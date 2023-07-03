fish
=========

An Ansible role to install and configure fish.

Requirements
------------

None

Role Variables
--------------

`fish_key_id`: The identifier of the key

`fish_key_url`: The URL to retrieve gpg key

`fish_key_path`: The keyring path (default: /usr/share/keyrings/fish.gpg)

`fish_repo_url`: A source string for the repository

`fisher`: Install fisher

`fisher_package_name`: Fisher package name (default: "jorgebucaran/fisher")

`fisher_url`: Fisher repository

`fisher_install_plugins`: Install plugins

`fisher_plugins`: Plugins list


Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.fish, fisher: true }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
