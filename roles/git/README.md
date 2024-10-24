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

`git_user_signingkey`: Signing key

`git_commit_gpgsign`: Sign all commits

`git_tag_gpgsign`: Sign all tags

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
