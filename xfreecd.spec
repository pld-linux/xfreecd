Summary:	Xfreecd, a CD player with CDDB features
Summary(pl):	Xfreecd - odtwarzacz p³yt audio ze wsparciem dla CDDB
Name:		xfreecd
Version:	0.7.7
Release:	3
Copyright:	GPL
Group:		X11/Amusements
Group(pl):	X11/Rozrywka
URL:		http://www.tatoosh.com/nexus/xfreecd.shtml
Source:		http://www.tatoosh.com/nexus/linux/%{name}-%{version}.tar.gz
Patch0:		xfreecd.patch
Patch1:		xfreecd-gtk.patch
Icon:		xfreecd.gif
BuildPrereq:	XFree86-devel
BuildPrereq:	gtk+-devel
BuildPrereq:	glib-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
XfreeCD is a X windows program written using GTK+ that looks like the
frontpanel of a cd player. It also supports the CDDB database of CD track
information, and is certified for submitting new CD information to the
database. At 137x90 it takes up a small amount of screen space.

%description -l pl
Xfreecd jest odtwarzaczem p³yt audio opartym o bibliotekê GTK+.
Korzysta on z bazy danych CDDB zawieraj±cej informacje o p³ytach CD.
Mo¿e on dodawaæ swoje zapisy do takiej bazy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,include/X11/pixmaps}}

install -s xfreecd $RPM_BUILD_ROOT/usr/X11R6/bin
install xfreecd.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xfreecd
install xfreecd.xpm $RPM_BUILD_ROOT/usr/X11R6/include/X11/pixmaps

gzip -9nf README HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,HISTORY}.gz
/etc/X11/wmconfig/xfreecd

%attr(755,root,root) /usr/X11R6/bin/xfreecd
/usr/X11R6/include/X11/pixmaps/xfreecd.xpm

%changelog
* Thu May 13 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.7.7-3]
- removed %config from wmconfig file,
- added BuildPrereq rules,
- added xfreecd-gtk.patch,
- fixed passing RPM_OPT_FLAGS,
- removed LDFLAGS=-s,
- rebuild on rpm 3.

* Thu Apr 15 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.7.7-2]
- added Group(pl)
- added gzipping documentation
- added %config(missingok) for wmconfig file
- added LDFLAGS=-s

* Mon Sep 21 1998 Pawe³ Gajda <pagaj@shadow.eu.org>
- added pl translation,
- patched to make it compile with RPM_OPT_FLAGS.
