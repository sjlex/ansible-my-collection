bat
=========

An Ansible role to install and configure bat.

Requirements
------------

None

Role Variables
--------------

`bat_package_version`: Package version

`bat_package_url`: Package URL

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.bat, bat_package_version: '0.23.0' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
