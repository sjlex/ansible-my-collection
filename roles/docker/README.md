docker
=========

An Ansible role to install and configure docker.

Requirements
------------

None

Role Variables
--------------

`docker_key_id`: The identifier of the key

`docker_key_url`: The URL to retrieve gpg key

`docker_key_path`: The keyring path (default: /usr/share/keyrings/docker.gpg)

`docker_repo_url`: A source string for the repository

`docker_host_tcp`: Use daemon socket (default: false)

`docker_host_url`: Daemon socket to connect to (default: tcp://localhost:2375)

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.docker, docker_repo_url: 'https://download.docker.com/linux/debian' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
