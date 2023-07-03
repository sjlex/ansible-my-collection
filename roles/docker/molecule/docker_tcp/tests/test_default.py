import pytest


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("root", "/etc/profile.d/docker.sh"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user
    assert config.contains("export DOCKER_HOST=tcp://localhost:2375")


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_docker_host(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        echo $DOCKER_HOST
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout == "tcp://localhost:2375\n"
