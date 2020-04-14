import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sslscan_package_installed(host):
    assert host.package("sslscan").is_installed


def test_sslscan_binary_exists(host):
    assert host.file('/usr/bin/sslscan').exists


def test_sslscan_binary_file(host):
    assert host.file('/usr/bin/sslscan').is_file


def test_sslscan_binary_which(host):
    assert host.check_output('which sslscan') == '/usr/bin/sslscan'
