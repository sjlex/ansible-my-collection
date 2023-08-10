import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        btop --help
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "buster", "btop", "1.2.13"),
        ("debian", "bullseye", "btop", "1.2.13"),
        ("debian", "bookworm", "btop", "1.2.13"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("btop --version")

        assert cmd.rc == 0
        assert cmd.stdout.startswith(f"btop version: {package_version}\n")
