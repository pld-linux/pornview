Summary:	jpeg file viewer
Summary(pl):	Przegl±darka jpegów
Name:		pornview
Version:	0.2.0
Release:	0.pre1.2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}pre1.tar.gz
# Source0-md5:	339fde6d7ff0cc1053abe951601373e6
URL:		http://pornview.sourceforge.net/
Patch0:		%{name}-no_libcharset.patch
Patch1:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	xine-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PornView is a jpeg file viewer. Basic features:
- thumbnails,
- slideshow,
- fullscreen,
- support movies.

%description -l pl
PornView jest przegl±dark± jpegów. Podstawowe w³a¶ciwo¶ci:
- miniaturki,
- slideshow,
- wy¶wietlanie pe³noekranowe,
- odtwarzanie filmów.

%prep
%setup -q -n %{name}-%{version}pre1
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-xine

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Graphics/* $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
