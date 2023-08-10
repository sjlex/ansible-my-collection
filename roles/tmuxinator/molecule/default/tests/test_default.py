import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        tmuxinator version
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.startswith("tmuxinator")


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "buster", "tmuxinator", "0.15"),
        ("debian", "bullseye", "tmuxinator", "2.0"),
        ("debian", "bookworm", "tmuxinator", "3.0"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename
    host_package = host.package(package_name)

    if host_os == os_name and os_codename == host_os_codename:
        assert host_package.version.startswith(package_version)

    assert host_package.is_installed
