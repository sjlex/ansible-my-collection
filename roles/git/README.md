git
=========

An Ansible role to install and configure git.

Requirements
------------

None

Role Variables
--------------

`git_user_name`: User name

`git_user_email`: Email address

`git_core_autocrlf`: Autocrlf (default: input)

`git_core_filemode`: Filemode (default: false)

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.git, git_user_name: 'User' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
