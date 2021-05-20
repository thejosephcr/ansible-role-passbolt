# ansible-role-passbolt

[![Build Status](https://github.com/wpnops/ansible-role-passbolt/workflows/CI/badge.svg)](https://github.com/wpnops/ansible-role-passbolt/actions)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-wpnops.ansible-role-passbolt.vim-blue.svg)](https://galaxy.ansible.com/wpnops/ansible-role-passbolt/)

An [ansible role](https://galaxy.ansible.com/wpnops/passbolt) to install and configure ansible-role-passbolt

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Dependencies

By default this role does depend on someone external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

## Example Playbook

- hosts: servers
  roles:
     - role: wpnops.ansible-role-passbolt
       ansible_role_passbolt_package_state: latest

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):

  * Ubuntu Focal

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
