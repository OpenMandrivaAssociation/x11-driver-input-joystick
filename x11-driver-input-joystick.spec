Name: x11-driver-input-joystick
Version: 1.3.0
Release: %mkrel 3
Summary: X.org input driver for joysticks
Group: System/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-joystick  xorg/drivers/xf86-input-joystick
# cd xorg/drivers/xf86-input/joystick
# git-archive --format=tar --prefix=xf86-input-joystick-1.3.0/ master | bzip2 -9 > xf86-input-joystick-1.3.0.tar.bz2
########################################################################
Source0: xf86-input-joystick-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
Joystick is an X.org input driver for joysticks.

%prep
%setup -q -n xf86-input-joystick-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/joystick_drv.la
%{_libdir}/xorg/modules/input/joystick_drv.so
%_mandir/man4/*

