# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, Dict, List, Optional, Union, TYPE_CHECKING
##from ansible_collections.oxide.computer.plugins.module_utils.session import Session
##from ansible_collections.oxide.computer.plugins.module_utils.models import SshKeyCreate
from ansible_collections.oxide.computer.plugins.module_utils.models import *

if TYPE_CHECKING:
    from ansible_collections.oxide.computer.plugins.module_utils.oxide_region_api  import OxideRegionAPI


class CurrentUserSshKeyCreate:
    def __init__(self, parent: "OxideRegionAPI"):
        self.parent = parent

    def current_user_ssh_key_create(
        self,
        description: str,
        name: Name,
        public_key: str,
    ) -> Any:
        """
        Create an SSH public key for the currently authenticated user.

        Args:
            description: Create-time parameters for an `SshKey`
            name: Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and '-', and may not end with a '-'. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long.
            public_key: SSH public key, e.g., `"ssh-ed25519 AAAAC3NzaC..."`

        Returns:
            Response data
        """
        path = f"/v1/me/ssh-keys"
        params = None
        headers = None
        json_data = {
            "description": description if description is not None else None,
            "name": name if name is not None else None,
            "public_key": public_key if public_key is not None else None,
        }
        json_data = {k: v for k, v in json_data.items() if v is not None}

        response = self.parent._make_request(
            method="POST",
            path=path,
            params=params,
            headers=headers,
            json_data=json_data,
        )
        return response.json()
