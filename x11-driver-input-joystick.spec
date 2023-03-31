Name:		x11-driver-input-joystick
Version:	1.6.3
Release:	4
Summary:	X.org input driver for joysticks
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-joystick-%{version}.tar.bz2
License:	MIT
Patch0:		xf86-input-joystick-1.6.2-link-against-xi.patch
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.18
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xi)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Conflicts:	xorg-x11-server < 7.0

%description
Joystick is an X.org input driver for joysticks.

%prep
%setup -qn xf86-input-joystick-%{version}
%autopatch -p1

%build
autoreconf -fiv
%configure --prefix=/usr
%make

%install
%makeinstall_std

#(eandry) remove devel file, create a devel package if needed
rm -rf %{buildroot}%{_includedir}/xorg/*.h
rm -rf %{buildroot}%{_libdir}/pkgconfig/*.pc
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/input/joystick_drv.so
%_mandir/man4/*
