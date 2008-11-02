Summary: Poor man's version control.
Name: pvc
Version: 1.0
Release: 1
Packager: KELEMEN Peter <Peter.Kelemen@gmail.com>
License: GPL
Group: Applications/System

Requires: bash, net-tools, coreutils, diff, sed

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/sbin/pvc
/usr/share/man/man8
%doc /usr/share/doc/%{name}-%{version}/README
%doc /usr/share/doc/%{name}-%{version}/COPYING

%files -n apt-pvc
%defattr(-,root,root)
/usr/sbin/apt-pvc
/usr/share/man/man8

%post

%changelog
* Sun Nov  2 2008  KELEMEN Peter <Peter.Kelemen@gmail.com> 1.0-1
- Initial release.
