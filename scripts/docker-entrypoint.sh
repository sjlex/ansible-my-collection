#!/usr/bin/env bash
set -eu

DOCKER_SOCKET_SOURCE=/var/docker.sock
DOCKER_SOCKET_TARGET=/var/run/docker.sock

# bashrc
mkdir -p /etc/profile.d
echo -e "\
cd $PWD \n\
ln -sfn $DOCKER_SOCKET_SOURCE $DOCKER_SOCKET_TARGET \n\
source $(poetry env info --path)/bin/activate \n\
" | tee -a /etc/bash.bashrc > /dev/null

# systemd
if [ "$1" = '/sbin/init' ]; then
  exec /sbin/init "$@"
fi

exec "$@"
