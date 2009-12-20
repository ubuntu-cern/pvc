Summary: Poor man's version control.
Name: pvc
Version: 1.3
Release: 1
Packager: KELEMEN Peter <Peter.Kelemen@gmail.com>
License: GPL2
Group: Applications/System

Requires: bash, net-tools, coreutils, diffutils, sed

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Source: %{name}-%{version}.tar.gz
Prefix: /

%description
Minimal configuration management utility to track changes.  Provides a
convenient way for multiple system administrators to keep a log of changes
and modified files.

%package -n apt-pvc
Summary: Wrapper around apt-get to log actions using pvc.
Group: Applications/System
Requires: mktemp, pvc, apt

%description -n apt-pvc
Wrapper around apt-get to log actions using pvc.

%prep
%setup -n %{name}-%{version}
make 

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/etc/sysconfig
cp env.sh %{buildroot}/etc/sysconfig/pvc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755,root,root) /usr/sbin/pvc
/usr/sbin/changelog
/usr/sbin/mod
/usr/share/man/man8/pvc.8.gz
/usr/share/man/man8/changelog.8.gz
/usr/share/man/man8/mod.8.gz
%doc /usr/share/doc/%{name}-%{version}/README
%doc /usr/share/doc/%{name}-%{version}/COPYING
%config /etc/sysconfig/pvc

%files -n apt-pvc
%defattr(-,root,root)
%attr(755,root,root) /usr/sbin/apt-pvc
/usr/share/man/man8/apt-pvc.8.gz

%post

%changelog
* Sun Dec 20 2009  FROHNER Akos <akos@frohner.hu> 1.3-1
- default settings in /etc/sysconfig

* Tue Nov 11 2008  FROHNER Akos <akos@frohner.hu> 1.2-2
- diff is packaged as 'diffutils'
- adding executable permissions

* Mon Nov  3 2008  KELEMEN Peter <Peter.Kelemen@gmail.com> 1.2-1
- Bump version number.

* Mon Nov  3 2008  KELEMEN Peter <Peter.Kelemen@gmail.com> 1.1-1
- Bump version number.

* Mon Nov  3 2008  KELEMEN Peter <Peter.Kelemen@gmail.com> 1.0-2
- Add missing changelog(8) and mod(8) symlinks.
- Add apt-pvc.8 manpage.

* Sun Nov  2 2008  KELEMEN Peter <Peter.Kelemen@gmail.com> 1.0-1
- Initial release.
