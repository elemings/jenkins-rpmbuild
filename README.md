# jenkins-rpmbuild

## Official Jenkins Release Distribution

http://mirrors.jenkins-ci.org/war-stable/latest/

## "Official" Jenkins RPM Builds

https://github.com/jenkinsci/packaging/tree/master/rpm

### Build Procedure

$ export WAR=/path/to/jenkins.war/file
$ make rpm BRAND=./branding/jenkins.mk
$ ls ./target/rpm

### Documentation

https://pkg.jenkins.io/redhat-stable/

### Notes

- Uses old SysV init scripts.
- HTTPS support has to be manually configured.

## Red Hat Open Shift

Consists of two separate RPMS: the Jenkins core and a bundle of Jenkins plugins.

### SRPMS

http://ftp.redhat.com/redhat/linux/enterprise/7Server/en/RHOSE/SRPMS/

### Notes

- Uses newer systemd files.
- Had HTTPS support but this was removed.


