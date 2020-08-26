# TODO:
# - how to add to the trusted service of the firewall?

%define _prefix	%{_usr}/lib/jenkins
%define _pkgsharedstatedir	%{_var}/lib/jenkins

Name:		jenkins
Version:	2.235.5
Release:	1%{?dist}
Summary:	Continous Build Server
Source:		http://mirrors.jenkins-ci.org/war-stable/%{version}/%{name}.war
Source1:	jenkins.init.in
Source2:	jenkins.sysconfig.in
Source3:	jenkins.logrotate
Source5:	jenkins.service.in
Source6:	jenkins.prestart.in
Source7:	jenkins.jks
URL:		http://jenkins.io/
Group:		Development/Tools/Building
License:	MIT/X License, GPL/CDDL, ASL2
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
Obsoletes:	hudson
BuildRequires:	shadow-utils
%if 0%{?rhel} >= 7
BuildRequires:	systemd
%endif
Requires:	shadow-utils
BuildArch:	noarch

%description
Jenkins monitors executions of repeated jobs, such as building a software
project or jobs run by cron. Among those things, current Jenkins focuses on the
following two jobs:
- Building/testing software projects continuously, just like CruiseControl or
  DamageControl. In a nutshell, Jenkins provides an easy-to-use so-called
  continuous integration system, making it easier for developers to integrate
  changes to the project, and making it easier for users to obtain a fresh
  build. The automated, continuous build increases the productivity.
- Monitoring executions of externally-run jobs, such as cron jobs and procmail
  jobs, even those that are run on a remote machine. For example, with cron,
  all you receive is regular e-mails that capture the output, and it is up to
  you to look at them diligently and notice when it broke. Jenkins keeps those
  outputs and makes it easy for you to notice when something is wrong.

%prep
%setup -q -T -c

%build

%install
rm -rf "%{buildroot}"
%__install -D -m0644 "%{SOURCE0}" "%{buildroot}%{_prefix}/%{name}.war"
%__install -d "%{buildroot}%{_pkgsharedstatedir}"
%__install -d "%{buildroot}%{_pkgsharedstatedir}/plugins"

%__install -d "%{buildroot}/var/log/%{name}"
%__install -d "%{buildroot}/var/cache/%{name}"

%if 0%{?rhel} >= 7
install -d -m 0755 %{buildroot}%{_unitdir}
%__install -D -m0644 "%{SOURCE5}" "%{buildroot}%{_unitdir}/%{name}.service"
%__install -D -m0755 "%{SOURCE6}" "%{buildroot}%{_unitdir}/%{name}.prestart"
%__sed -i 's,@@WAR@@,%{_prefix}/%{name}.war,g' "%{buildroot}%{_unitdir}/%{name}.service"
%__sed -i 's,@@WAR@@,%{_prefix}/%{name}.war,g' "%{buildroot}%{_unitdir}/%{name}.prestart"
%else
%__install -D -m0755 "%{SOURCE1}" "%{buildroot}/etc/init.d/%{name}"
%__sed -i 's,@@WAR@@,%{_prefix}/%{name}.war,g' "%{buildroot}/etc/init.d/%{name}"
%__install -d "%{buildroot}/usr/sbin"
%__ln_s "../../etc/init.d/%{name}" "%{buildroot}/usr/sbin/rc%{name}"
%endif

%__install -D -m0600 "%{SOURCE7}" "%{buildroot}/etc/pki/java/%{name}"

%__install -D -m0600 "%{SOURCE2}" "%{buildroot}/etc/sysconfig/%{name}"
%__sed -i 's,@@HOME@@,%{_pkgsharedstatedir},g' "%{buildroot}/etc/sysconfig/%{name}"

%__install -D -m0644 "%{SOURCE3}" "%{buildroot}/etc/logrotate.d/%{name}"

%pre
/usr/sbin/groupadd -r %{name} &>/dev/null || :
# SUSE version had -o here, but in Fedora -o isn't allowed without -u
/usr/sbin/useradd -g %{name} -s /bin/false -r -c "Jenkins Continuous Build server" \
	-d "%{_pkgsharedstatedir}" %{name} &>/dev/null || :

%post
%if 0%{?rhel} >= 7
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}

# If we have an old hudson install, rename it to jenkins
if test -d /var/lib/hudson; then
    # leave a marker to indicate this came from Hudson.
    # could be useful down the road
    # This also ensures that the .??* wildcard matches something
    touch /var/lib/hudson/.moving-hudson
    mv -f /var/lib/hudson/* /var/lib/hudson/.??* /var/lib/jenkins
    rmdir /var/lib/hudson
    find /var/lib/jenkins -user hudson -exec chown jenkins {} + || true
fi
if test -d /var/run/hudson; then
    mv -f /var/run/hudson/* /var/run/jenkins
    rmdir /var/run/hudson
fi
%endif

%preun
%if 0%{?rhel} >= 7
%systemd_preun %{name}.service
%else
if [ "$1" = 0 ] ; then
    # if this is uninstallation as opposed to upgrade, delete the service
    /sbin/service %{name} stop > /dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi
exit 0
%endif

%postun
%if 0%{?rhel} >= 7
%systemd_postun
%else
if [ "$1" -ge 1 ]; then
    /sbin/service %{name} condrestart > /dev/null 2>&1
fi
mv %{_pkgsharedstatedir} %{_pkgsharedstatedir}.`date +%s`
exit 0
%endif

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%dir %{_prefix}
%{_prefix}/%{name}.war
%attr(0755,%{name},%{name}) %dir %{_pkgsharedstatedir}
%attr(0750,%{name},%{name}) %{_var}/log/%{name}
%attr(0750,%{name},%{name}) %{_var}/cache/%{name}
%config /etc/logrotate.d/%{name}
%config(noreplace) /etc/sysconfig/%{name}
%attr(0640,%{name},%{name}) /etc/pki/java/%{name}
%if 0%{?rhel} >= 7
%{_unitdir}/%{name}.prestart
%{_unitdir}/%{name}.service
%else
%config(noreplace) /etc/init.d/%{name}
/usr/sbin/rc%{name}
%endif

%changelog
* Tue Aug 25 2020 Eric Lemings <eric@lemings.com> - 2.235.5-1
- Change _workdir to package-specific _sharedstatedir
- Update to 2.235.5
- Drop the epoch from version
- Add/Update web URLs
- Reference %{_var} in %files where appropriate

* Fri Jun 05 2020 Justin Pierce <jupierce@redhat.com> - 2.222.1.1591353286-1
- Update to 2.222.1.1591353286

* Thu Mar 05 2020 Justin Pierce <jupierce@redhat.com> - 2.204.2.1583447235-1
- Update to 2.204.2.1583447235

* Mon Feb 17 2020 Justin Pierce <jupierce@redhat.com> - 2.204.1.1581951349-1
- Update to 2.204.1.1581951349

* Wed Feb 05 2020 Justin Pierce <jupierce@redhat.com> - 2.204.2.1580892861-1
- Update to 2.204.2.1580892861

* Wed Jan 08 2020 Justin Pierce <jupierce@redhat.com> - 2.204.1.1578489705-1
- Update to 2.204.1.1578489705

* Tue Jan 07 2020 Justin Pierce <jupierce@redhat.com> - 2.176.4.1578403418-1
- Update to 2.176.4.1578403418

* Thu Dec 19 2019 Justin Pierce <jupierce@redhat.com> - 2.176.4.1576755573-1
- Update to 2.176.4.1576755573

* Wed Nov 27 2019 Justin Pierce <jupierce@redhat.com> - 2.176.4.1574865864-1
- Update to 2.176.4.1574865864

* Wed Sep 11 2019 Justin Pierce <jupierce@redhat.com> - 2.176.3.1568230904-1
- Update to 2.176.3.1568230904

* Thu Jul 18 2019 Justin Pierce <jupierce@redhat.com> - 2.176.2.1563461785-1
- Update to 2.176.2.1563461785

* Thu Apr 04 2019 Eric Lemings <eric@lemings.com> - 2.164.1.1554405920-3
- Replace HTTP protocol with HTTPS as default.

* Wed Mar 27 2019 Eric Lemings <eric@lemings.com> - 2.164.1.1553656760-2
- Translate sysconfig values into systemd Java command.

* Fri Feb 01 2019 Eric Lemings <eric@lemings.com> - 2.164.1.1552705448-1
- Update to 2.164.1.1552705448

* Fri Feb 01 2019 Justin Pierce <jupierce@redhat.com> - 2.150.2.1549032159-1
- Update to 2.150.2.1549032159

* Sun Dec 09 2018 Justin Pierce <jupierce@redhat.com> - 2.138.4.1544416383-1
- Update to 2.138.4.1544416383

* Mon Nov 12 2018 Justin Pierce <jupierce@redhat.com> - 2.138.2.1542054911-1
- Update to 2.138.2.1542054911

* Wed Aug 15 2018 Justin Pierce <jupierce@redhat.com> - 2.121.3.1534368708-1
- Update to 2.121.3.1534368708

* Fri Jul 20 2018 Justin Pierce <jupierce@redhat.com> - 2.121.2.1532143128-1
- Update to 2.121.2.1532143128

* Mon Jun 11 2018 Justin Pierce <jupierce@redhat.com> - 2.121.1.1528724062-1
- Update to 2.121.1.1528724062

* Tue Dec 19 2017 Justin Pierce <jupierce@redhat.com> - 2.89.2-1
- Update to 2.89.2

* Tue Dec 19 2017 Justin Pierce <jupierce@redhat.com> - 2.89.2-1
- Update to 2.89.2

* Tue Dec 12 2017 Samuel Munilla <smunilla@redhat.com - 2.89.1-1
- Update to 2.89.1

* Wed Nov 8 2017 Samuel Munilla <smunilla@redhat.com - 2.73.3-1
- Update to 2.73.3

* Mon Sep 25 2017 Samuel Munilla <smunilla@redhat.com - 2.73.1-1
- Update to 2.73.1

* Tue May 30 2017 Troy Dawson <tdawson@redhat.com> - 2.46.3-1
- Update to 2.46.3

* Mon May 08 2017 Troy Dawson <tdawson@redhat.com> - 2.46.2-1
- Update to 2.46.2
-- Fixes CVE-2017-1000353 CVE-2017-1000354
-- Fixes CVE-2017-1000355 CVE-2017-1000356
-- Fixes at least 21 security issues


* Tue Apr 04 2017 Troy Dawson <tdawson@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Thu Feb 02 2017 Troy Dawson <tdawson@redhat.com> - 2.32.2-1
- Update to 2.32.2
-- Fixes CVE-2017-2602 CVE-2017-2603 CVE-2017-2604 CVE-2017-2605
-- Fixes CVE-2017-2606 CVE-2017-2607 CVE-2017-2608 CVE-2017-2609
-- Fixes CVE-2017-2610 CVE-2017-2611 CVE-2017-2612 CVE-2017-2613
-- Fixes at least 20 security issues

* Fri Nov 18 2016 Troy Dawson <tdawson@redhat.com> - 2.19.3-1
- Update to 2.19.3
-- Fixes CVE-2016-9299
-- Fixes many other security issues

* Thu Sep 22 2016 Troy Dawson <tdawson@redhat.com> - 2.7.4-1
- Update to 2.7.4

* Wed Mar 02 2016 Troy Dawson <tdawson@redhat.com> - 1.651.2-1
- Update to 1.651.2 for quarterly update
-- Fixes over 7 security issues

* Wed Mar 02 2016 Troy Dawson <tdawson@redhat.com> - 1.642.2-1
- Update to 1.642.2 for quarterly update
-- Fixes over 5 security issues

* Mon Feb 01 2016 Troy Dawson <tdawson@redhat.com> - 1.642.1-1
- Update to 1.642.1

* Fri Jan 15 2016 Troy Dawson <tdawson@redhat.com> - 1.625.3-3
- systemd on rhel7+, init.d on everything else

* Thu Jan 14 2016 Troy Dawson <tdawson@redhat.com> - 1.625.3-2
- Update release for rebuild

* Wed Dec 23 2015 Scott Dodson <sdodson@redhat.com> - 1.625.3-1
- Update to 1.625.3
-- Fixes over 4 security issues
- This version requires java 7+

* Thu Oct 02 2014 Troy Dawson <tdawson@redhat.com> - 1.565.3-1
- Upgrade to 1.565.3 LTS
-- Fixes over 13 security issues

* Tue Jun 24 2014 Troy Dawson <tdawson@redhat.com> - 1.554.2-1
- Upgrade to 1.554.2 LTS

* Mon Dec 16 2013 Troy Dawson (tdawson@redhat.com) - 1.532.1-1
- Upgrade to 1.532.1 LTS

* Fri May 03 2013 Troy Dawson (tdawson@redhat.com) - 1.509.1-1
- Upgrade to 1.509.1 LTS this fixes
  CVE-2013-0253 CVE-2013-1808
  CVE-2013-2033 CVE-2013-2034

* Fri Mar 08 2013 Adam Miller <admiller@redhat.com>
- Upgrade to 1.480.3 LTS for CVE-2013-0327 CVE-2013-0328 CVE-2013-0329 
  CVE-2013-0330 CVE-2013-0331 
- Add dist-tag

* Tue Jan 08 2013 Adam Miller <admiller@redhat.com>
- Move to 1.480.2 LTS release for CVE-2012-6072

* Wed Sep 26 2012 Wesley Hearn
- Bumped to 1.483

* Thu Apr 12 2012 Troy Dawson (tdawson@redhat.com)
- Changed %{ver} to a real version number
- Removed Source4: jenkins.repo
- Removed installing Source4
- Removed files line for jenkins.repo

* Wed Sep 28 2011 kk@kohsuke.org
- See [http://jenkins-ci.org/changelog] for complete details
