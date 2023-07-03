lazydocker
=========

An Ansible role to install and configure lazydocker.

Requirements
------------

None

Role Variables
--------------

`lazydocker_package_version`: Package version

`lazydocker_package_url`: Package URL

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.lazydocker, lazydocker_package_version: '0.20.0' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
