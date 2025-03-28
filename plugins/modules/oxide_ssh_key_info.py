#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oxide.computer.plugins.module_utils.oxide_region_api import OxideRegionAPI
from ansible_collections.oxide.computer.plugins.module_utils.session import Session

def main():
    module_args = dict(
        name=dict(type="str", required=False),
        oxide_host=dict(type="str", required=True),
        oxide_token=dict(type="str", required=True, no_log=True),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    name = module.params["name"]
    oxide_host = module.params["oxide_host"]
    oxide_token = module.params["oxide_token"]

    try:
        api = OxideRegionAPI(base_url=oxide_host, api_key=oxide_token)
        session = Session(parent=api)

        keys_response = session.current_user_ssh_key_list.current_user_ssh_key_list()
        all_keys = keys_response.get("items", [])

        if name:
            matched_keys = [key for key in all_keys if key["name"] == name or key.get("id") == name]
            ssh_key = matched_keys[0] if matched_keys else None
            module.exit_json(changed=False, ssh_key=ssh_key)
        else:
            module.exit_json(changed=False, ssh_keys=all_keys)

    except Exception as e:
        module.fail_json(msg="Failed to retrieve SSH key information", error=str(e))

if __name__ == "__main__":
    main()
