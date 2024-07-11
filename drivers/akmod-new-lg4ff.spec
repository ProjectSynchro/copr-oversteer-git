%define module new-lg4ff

Name:       akmod-%{module}
Version:    0.4.1
Release:    1%{?dist}
Summary:    Automatic kernel module for %{module}

License:    GPLv3
URL:        https://github.com/berarma/new-lg4ff
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz#/%{module}-%{version}.tar.gz

BuildRequires:  kernel-devel
Requires:       akmod

%description
This package provides an automatic kernel module for %{module}.

%prep
%autosetup -n %{module}-%{version}

%build
# Build the kernel module using DKMS-style commands
make KVERSION=$kernelver %{?_smp_mflags}

%install
# Install the module
make INSTALL_MOD_DIR=updates modules_install \
    INSTALL_MOD_PATH=%{buildroot} KVERSION=$kernelver

# Clean up unnecessary files
rm -rf %{buildroot}/lib/modules/%{version}/source
rm -rf %{buildroot}/lib/modules/%{version}/build

%files
%defattr(0644,root,root,-)
%dir /lib/modules/%{version}/updates/
/lib/modules/%{version}/updates/hid-logitech-new.ko

%post
/usr/sbin/akmods --force || :
/sbin/depmod -a $(uname -r) || :

%preun
if [ $1 -eq 0 ]; then
    /sbin/depmod -a $(uname -r) || :
fi

%changelog
* Thu Jul 11 2024 Jack Greiner <jack@emoss.org> - 0.4.1-1
- Initial spec file using 0.4.1

