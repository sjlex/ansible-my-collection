btop
=========

An Ansible role to install and configure btop.

Requirements
------------

None

Role Variables
--------------

`btop_package_version`: Package version

`btop_package_url`: Package URL

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.btop, btop_package_version: '1.2.13' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
