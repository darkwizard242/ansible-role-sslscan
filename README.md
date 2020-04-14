[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-sslscan.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-sslscan) ![Ansible Role](https://img.shields.io/ansible/role/42038?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/42038?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/42038?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-sslscan&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-sslscan) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-sslscan?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-sslscan?color=orange&style=flat-square)

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

Variable              | Value (default) | Description
--------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
sslscan_app           | sslscan         | Defines the app to install i.e. **sslscan**
sslscan_desired_state | present         | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
