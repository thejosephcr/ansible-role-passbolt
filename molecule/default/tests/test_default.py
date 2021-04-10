def test_command(host):
    assert host.command('ansible-role-passbolt --version').rc == 0
