broot
=========

An Ansible role to install and configure broot.

Requirements
------------

None

Role Variables
--------------

`broot_package_version`: Package version

`broot_package_url`: Package URL

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.broot, broot_package_version: '1.24.1' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
