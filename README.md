# Oxide Computer Collection
This repository contains a POC Oxide Ansible Collection. It is a bit of a mess at the moment. I have also POC'd a [rust based binary module](https://github.com/jforce/oxide_ansible_rust_module), however, I'm not sure which way is most ideal to go with.

## Modules
| Module         | Description                                |
|----------------|--------------------------------------------|
| oxide_disk     | Create and delete different types of disks |
| oxide_image    | Create images from snapshots               |
| oxide_project  | Manage projects                            |
| oxide_snapshot | Manage snapshots                           |
| oxide_ssh_key  | Manage user SSH keys                       |
| oxide_instance | Manage compute instances (fairly minimal)  |

## Using this collection
See [installing collections](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html) and [using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

Authentication requires a token which can be obtained using the Oxide CLI:
```bash
oxide auth status --show-token
```

## More information
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible Collections Checklist](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
- [The Bullhorn (the Ansible Contributor newsletter)](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420)
- [News for Maintainers](https://github.com/ansible-collections/news-for-maintainers)
