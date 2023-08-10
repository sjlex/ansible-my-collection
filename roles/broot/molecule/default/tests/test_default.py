import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        broot --help
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "buster", "broot", "1.24.1"),
        ("debian", "bullseye", "broot", "1.24.1"),
        ("debian", "bookworm", "broot", "1.24.1"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("broot --version")

        assert cmd.rc == 0
        assert cmd.stdout.startswith(f"broot {package_version}\n")


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("ansible", "/home/ansible/.config/broot/conf.hjson"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user
    assert config.contains('default_flags: "hip"')
    assert config.contains("modal: true")
