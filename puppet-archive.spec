%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%global commit 2f4cb0fb9e557da6e0e63d631045d2d4c8fec730
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-archive
Version:                6.0.2
Release:                0.1%{?milestone}%{?alphatag}%{?dist}
Summary:                Compressed archive file download and extraction with native types/providers for Windows and Unix
License:                ASL 2.0

URL:                    https://github.com/voxpupuli/puppet-archive

Source0:                https://github.com/voxpupuli/puppet-archive/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet >= 4.6.1

%description
The archive module provides native puppet resources for managing compressed file download and extraction with optional checksum verification and cleanup.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

# puppet-archive includes a cacert file used when running in windows
# this cacert file is not needed for linux and it's not recommended to
# ship certificates in packages out of system ones so we are removing it
find . -name cacert.pem -exec rm {} +

%build

%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/archive/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/archive/

%files
%{_datadir}/openstack-puppet/modules/archive/

%changelog
* Tue Sep 28 2021 RDO <dev@lists.rdoproject.org> 6.0.2-0.1.0rc0.2f4cb0fgit
- Update to post 6.0.2 (2f4cb0fb9e557da6e0e63d631045d2d4c8fec730)

