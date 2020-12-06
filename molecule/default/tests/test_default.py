import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = "sslscan"
PACKAGE_BINARY = "/usr/bin/sslscan"


def test_sslscan_package_installed(host):
    """
    Tests if sslscan is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_sslscan_binary_exists(host):
    """
    Tests if sslscan binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_sslscan_binary_file(host):
    """
    Tests if sslscan binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_sslscan_binary_which(host):
    """
    Tests the output to confirm sslscan's binary location.
    """
    assert host.check_output('which sslscan') == PACKAGE_BINARY
