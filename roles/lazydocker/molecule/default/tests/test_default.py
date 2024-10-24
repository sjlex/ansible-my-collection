import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        lazydocker --help
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "buster", "lazydocker", "0.23.3"),
        ("debian", "bullseye", "lazydocker", "0.23.3"),
        ("debian", "bookworm", "lazydocker", "0.23.3"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("lazydocker --version")

        assert cmd.rc == 0
        assert cmd.stdout.startswith(f"Version: {package_version}\n")
