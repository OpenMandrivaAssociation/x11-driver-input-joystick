Name: x11-driver-input-joystick
Version: 1.6.0
Release: %mkrel 2
Summary: X.org input driver for joysticks
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-joystick-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

Conflicts: xorg-x11-server < 7.0

%description
Joystick is an X.org input driver for joysticks.

%prep
%setup -q -n xf86-input-joystick-%{version}

%build
%configure2_5x --prefix=/usr
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#(eandry) remove devel file, create a devel package if needed
rm -rf %{buildroot}%{_includedir}/xorg/*.h
rm -rf %{buildroot}%{_libdir}/pkgconfig/*.pc

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/joystick_drv.la
%{_libdir}/xorg/modules/input/joystick_drv.so
%_mandir/man4/*
