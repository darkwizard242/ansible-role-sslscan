[![build-test](https://github.com/darkwizard242/ansible-role-sslscan/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-sslscan/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-sslscan/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-sslscan/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/sslscan) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-sslscan&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-sslscan) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-sslscan&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-sslscan) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-sslscan&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-sslscan) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-sslscan?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-sslscan?color=orange&style=flat-square)

# Ansible Role: sslscan

Role to install (_by default_) [sslscan](https://github.com/rbsec/sslscan) or uninstall (_if passed as var_) on Debian based and EL based systems. Sslscan is used for performing SSL/TLS scans.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
sslscan_app: sslscan
sslscan_desired_state: present
```

### Variables table:

Variable              | Description
--------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
sslscan_app           | Defines the app to install i.e. **sslscan**
sslscan_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **sslscan** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.sslscan
```

For customizing behavior of role (i.e. installation of latest **sslscan** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.sslscan
  vars:
    sslscan_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **sslscan** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.sslscan
  vars:
    sslscan_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-sslscan/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
