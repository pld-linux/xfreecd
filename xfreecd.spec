Summary:	Xfreecd, a CD player with CDDB features
Summary(pl):	Xfreecd - odtwarzacz p³yt audio ze wsparciem dla CDDB
Name:		xfreecd
Version:	0.7.8
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www.brianlane.com/linux/%{name}-%{version}.tar.gz
# Source0-md5:	96edec5a4586a251da32923ac9c8caa9
Patch0:		%{name}.patch
Patch1:		%{name}-gtk.patch
Icon:		xfreecd.gif
URL:		http://www.brianlane.com/linux/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XfreeCD is a X Window program written using GTK+ that looks like the
frontpanel of a cd player. It also supports the CDDB database of CD
track information, and is certified for submitting new CD information
to the database. At 137x90 it takes up a small amount of screen space.

%description -l pl
Xfreecd jest odtwarzaczem p³yt audio opartym o bibliotekê GTK+.
Korzysta on z bazy danych CDDB zawieraj±cej informacje o p³ytach CD.
Mo¿e on dodawaæ swoje zapisy do takiej bazy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/X11/pixmaps} \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.wmconfig $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/%{name}
install %{name}.xpm $RPM_BUILD_ROOT%{_includedir}/X11/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%{_sysconfdir}/X11/wmconfig/%{name}

%attr(755,root,root) %{_bindir}/%{name}
%{_includedir}/X11/pixmaps/%{name}.xpm
