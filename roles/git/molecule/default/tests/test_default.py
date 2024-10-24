import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        git --version
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.startswith("git version 2.")


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "buster", "git", "1:2"),
        ("debian", "bullseye", "git", "1:2"),
        ("debian", "bookworm", "git", "1:2"),
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
        ("ansible", "/home/ansible/.gitconfig"),
        ("ansible", "/home/ansible/.gitignore"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user


@pytest.mark.parametrize(
    "user,config_param",
    [
        ("ansible", "core.autocrlf"),
        ("ansible", "core.filemode"),
        ("ansible", "user.name"),
        ("ansible", "user.email"),
        ("ansible", "user.signingkey"),
        ("ansible", "commit.gpgsign"),
        ("ansible", "tag.gpgsign"),
    ],
)
def test_git_get_config(host, user, config_param):
    cmd = host.run(
        f"su - {user} -c %s",
        f"""/;
        git config --get {config_param}
        """,
    )

    assert cmd.rc == 0

    if config_param == "user.name":
        assert cmd.stdout.startswith("Foo Bar")

    if config_param == "user.email":
        assert cmd.stdout.startswith("foo@bar.com")

    if config_param == "user.signingkey":
        assert cmd.stdout.startswith("1234")

    if config_param == "commit.gpgsign":
        assert cmd.stdout.startswith("true")

    if config_param == "tag.gpgsign":
        assert cmd.stdout.startswith("false")

    if config_param == "core.autocrlf":
        assert cmd.stdout.startswith("input")

    if config_param == "core.filemode":
        assert cmd.stdout.startswith("false")
