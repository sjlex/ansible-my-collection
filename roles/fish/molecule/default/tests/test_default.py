import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        fish --command 'id -un'
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.startswith(user)


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "buster", "fish", "3.6.1"),
        ("debian", "bullseye", "fish", "3.6.1"),
        ("debian", "bookworm", "fish", "3.6.1"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("fish --version")

        assert cmd.rc == 0
        assert cmd.stdout.startswith(f"fish, version {package_version}\n")
