Summary:     Xfreecd, a CD player with CDDB features
Summary(pl): Xfreecd - odtwarzacz p³yt audio ze wsparciem dla CDDB
Name:        xfreecd
Version:     0.7.7
Release:     1
Copyright:   GPL
Group:       X11/Amusements
Source:      http://www.tatoosh.com/nexus/linux/%{name}-%{version}.tar.gz
Patch:       xfreecd.patch
URL:         http://www.tatoosh.com/nexus/xfreecd.shtml
Icon:        xfreecd.gif
Buildroot:   /tmp/%{name}-%{version}-root

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
%patch -p1

%build
CFLAGS=$RPM_OPT_FLAGS make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,include/X11/pixmaps}}

install -s xfreecd $RPM_BUILD_ROOT/usr/X11R6/bin
install xfreecd.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xfreecd
install xfreecd.xpm $RPM_BUILD_ROOT/usr/X11R6/include/X11/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README HISTORY
/etc/X11/wmconfig/xfreecd
/usr/X11R6/include/X11/pixmaps/xfreecd.xpm
%attr(755, root, root) /usr/X11R6/bin/xfreecd

%changelog
* Mon Sep 21 1998 Pawe³ Gajda <pagaj@shadow.eu.org>
- added pl translation,
- patched to make it compile with RPM_OPT_FLAGS.
