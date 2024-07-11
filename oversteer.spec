%define debug_package %{nil}

Name:           oversteer
Version:        0.8.1
Release:        1%{?dist}
Summary:        Steering Wheel Manager for GNU/Linux

License:        GPL-3.0-only
URL:            https://github.com/berarma/oversteer
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  python3-gobject
BuildRequires:  python3-pyudev
BuildRequires:  python3-pyxdg
BuildRequires:  python3-evdev
BuildRequires:  python3-matplotlib
BuildRequires:  python3-scipy
BuildRequires:  python3-numpy
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros

%description
Oversteer manages steering wheels on Linux using the
features provided by the loaded modules.
It doesn't provide hardware support, you'll still need a
driver module that enables the hardware on Linux.

%prep
%autosetup

# Stray vim swap file managed to make it into the project
rm oversteer/.device_manager.py.swp

%build
%meson \
    -Dpython="%{python3}" \
    -Dudev_rules_dir="%{_udevrulesdir}"

%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
/usr/bin/oversteer
%{_datadir}/icons/hicolor/scalable/apps/org.berarma.Oversteer.svg
%{_datadir}/applications/org.berarma.Oversteer.desktop
%{_datadir}/metainfo/org.berarma.Oversteer.appdata.xml
%{_udevrulesdir}/99-thrustmaster-wheel-perms.rules
%{_udevrulesdir}/99-logitech-wheel-perms.rules
%{_udevrulesdir}/99-fanatec-wheel-perms.rules
%{python3_sitelib}/oversteer/main.css
%{python3_sitelib}/oversteer/main.ui
%pycached %{python3_sitelib}/oversteer/wheel_ids.py
%pycached %{python3_sitelib}/oversteer/combined_chart.py
%pycached %{python3_sitelib}/oversteer/linear_chart.py
%pycached %{python3_sitelib}/oversteer/performance_chart.py
%pycached %{python3_sitelib}/oversteer/gtk_handlers.py
%pycached %{python3_sitelib}/oversteer/device.py
%pycached %{python3_sitelib}/oversteer/device_manager.py
%pycached %{python3_sitelib}/oversteer/gtk_ui.py
%pycached %{python3_sitelib}/oversteer/signal.py
%pycached %{python3_sitelib}/oversteer/model.py
%pycached %{python3_sitelib}/oversteer/gui.py
%pycached %{python3_sitelib}/oversteer/application.py
%pycached %{python3_sitelib}/oversteer/test.py
%pycached %{python3_sitelib}/oversteer/__init__.py

%changelog
* Sat Mar 23 2024 Jan200101 <sentrycraft123@gmail.com> - 0.8.1-1
- Initial spec

