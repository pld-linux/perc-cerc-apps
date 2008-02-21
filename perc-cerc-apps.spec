# TODO:
# - subpackages!
# - init scripts
Summary:	MegaRAID/PERC controll tools
Summary(pl.UTF-8):	Oprogramowanie do zarządzania macierzami MegaRAID/PERC
Name:		perc-cerc-apps
Version:	6.03
Release:	0.1
License:	Unknown
Group:		Base
Source0:	http://ftp.us.dell.com/ide/%{name}-%{version}-A06.tar.gz
# Source0-md5:	c176585691b8d3066ac70cc711d554f4
URL:		http://linux.dell.com/storage.shtml#megaraid_scsi
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MegaRAID controll tools.

%description -l pl.UTF-8
Oprogramowanie do zarządzania macierzami MegaRAID/PERC.

%prep
%setup -q -c

%build
for r in *.rpm; do
	rpm2cpio $r | cpio -i -d
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install usr/sbin/* $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_sbindir}/*
