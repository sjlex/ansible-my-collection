import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        tmux -V
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.startswith("tmux")


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "buster", "tmux", "2.8"),
        ("debian", "bullseye", "tmux", "3.1"),
        ("debian", "bookworm", "tmux", "3.3"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename
    host_package = host.package(package_name)

    if host_os == os_name and os_codename == host_os_codename:
        assert host_package.version.startswith(package_version)

    assert host_package.is_installed


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("ansible", "/home/ansible/.tmux.conf"),
        ("ansible", "/home/ansible/.config/tmux/tmux.conf"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user
