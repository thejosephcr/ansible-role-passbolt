# ansible-role-passbolt

[![Build Status][(https://github.com/pokerops/ansible-role-passbolt/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/pokerops/ansible-role-passbolt/actions/workflows/main.yml)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-pokerops.passbolt.vim-blue.svg)](https://galaxy.ansible.com/pokerops/passbolt/)

An [ansible role](https://galaxy.ansible.com/pokerops/passbolt) to install and configure ansible-role-passbolt

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Dependencies

By default this role does depend on someone external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

## Example Playbook

```
- hosts: servers
  roles:
     - role: pokerops.passbolt
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):

  * Ubuntu Focal
  * Debian 10

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
