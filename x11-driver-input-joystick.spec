Name:		x11-driver-input-joystick
Version:	1.6.2
Release:	8
Summary:	X.org input driver for joysticks
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-joystick-%{version}.tar.bz2
License:	MIT
Patch0:		xf86-input-joystick-1.6.2-link-against-xi.patch
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xi)

Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

Conflicts:	xorg-x11-server < 7.0

%description
Joystick is an X.org input driver for joysticks.

%prep
%setup -qn xf86-input-joystick-%{version}
%apply_patches

%build
autoreconf -fiv
%configure2_5x --prefix=/usr
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



%changelog
* Mon Mar 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6.1-1
+ Revision: 784335
- version update 1.6.1

* Fri Dec 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.6.0-3
+ Revision: 748294
- rebuild
- cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.0-2
+ Revision: 703626
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.6.0-1
+ Revision: 683594
- New version 1.6.0.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-5
+ Revision: 671126
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.5.0-4mdv2011.0
+ Revision: 595749
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.5.0-3mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 1.5.0-2mdv2010.1
+ Revision: 464332
- rebuild for new xserver

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 1.5.0-1mdv2010.1
+ Revision: 463604
- new release

* Thu Apr 30 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.4.1-1mdv2010.0
+ Revision: 369175
- New version 1.4.1

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 1.4.0-2mdv2009.1
+ Revision: 352760
- use configure2_5x
- remove devel file, create a devel package if needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 1.4.0

  + Thierry Vignaud <tv@mandriva.org>
    - something's odd with %%configure
    - adjust file list for new man pages path
    - new release

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-2mdv2009.0
+ Revision: 265859
- rebuild early 2009.0 package (before pixel changes)

* Mon May 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.2-1mdv2009.0
+ Revision: 206300
- Update to upstream release 1.3.2.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.1-3mdv2008.1
+ Revision: 160485
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3.1-2mdv2008.1
+ Revision: 156580
- re-enable rpm debug packages support

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.1-1mdv2008.1
+ Revision: 155649
- Update to version 1.3.1 that should match
  http://xorg.freedesktop.org/archive/individual/driver/xf86-input-joystick-1.3.1.tar.bz2
  Git tag is xf86-input-joystick-1.3.0-1
- Remove .la file. Version 1.3.1 is available and should be updated as soon
  as the current problems are resolved.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 1.3.0-2mdv2008.1
+ Revision: 106461
- rebuild for new lzma

* Mon Oct 29 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3.0-1mdv2008.1
+ Revision: 102992
- new upstream version: 1.3.0

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.3-2mdv2008.1
+ Revision: 98641
- minor spec cleanup
- build against xserver 1.4

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.2.3-1mdv2008.0
+ Revision: 64744
- new release

* Mon Jul 09 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.2-1mdv2008.0
+ Revision: 50741
- new upstream version: 1.2.2

* Mon Apr 23 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2.1-1mdv2008.0
+ Revision: 17412
- new upstream bugfix release

* Fri Apr 20 2007 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2008.0
+ Revision: 16013
- new release

