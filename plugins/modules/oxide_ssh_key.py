#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oxide.computer.plugins.module_utils.oxide_region_api import OxideRegionAPI
from ansible_collections.oxide.computer.plugins.module_utils.session import Session

def main():
    module_args = dict(
        name=dict(type="str", required=True),
        public_key=dict(type="str", required=False),
        description=dict(type="str", required=False, default="Created by Ansible"),
        oxide_host=dict(type="str", required=True),
        oxide_token=dict(type="str", required=True, no_log=True),
        state=dict(type="str", choices=["present", "absent"], default="present"),
    )

    result = dict(changed=False)
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    name = module.params["name"]
    public_key = module.params["public_key"]
    description = module.params["description"]
    oxide_host = module.params["oxide_host"]
    oxide_token = module.params["oxide_token"]
    state = module.params["state"]

    if state == "present" and not public_key:
        module.fail_json(msg="Parameter 'public_key' is required when state is 'present'")

    try:
        api = OxideRegionAPI(base_url=oxide_host, api_key=oxide_token)
        session = Session(parent=api)
        existing_keys = session.current_user_ssh_key_list.current_user_ssh_key_list()
        key_exists = any(k["name"] == name for k in existing_keys.get("items", []))

        if state == "present":
            if not key_exists:
                session.current_user_ssh_key_create(
                    name=name,
                    public_key=public_key,
                    description=description
                )
                result["changed"] = True
                result["msg"] = f"SSH key '{name}' created"
            else:
                result["msg"] = f"SSH key '{name}' already exists"

        elif state == "absent":
            if not key_exists:
                result["msg"] = f"SSH key '{name}' not found"
            else:
                try:
                    session.current_user_ssh_key_delete(ssh_key=name)
                    result.update(changed=True, msg=f"SSH key '{name}' deleted")
                except Exception as e:
                    module.fail_json(msg="Failed to delete SSH key", error=str(e), **result)

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg="Error managing SSH key", error=str(e), **result)

if __name__ == "__main__":
    main()
