Summary:	jpeg file viewer
Summary(pl):	Przegl�darka jpeg�w
Name:		pornview
Version:	0.1.3
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5: 7cbb2e651b75bb46c0f6b8808e7dc12a
URL:		http://pornview.sourceforge.net/
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
PornView jest przegl�dark� jpeg�w. Podstawowe w�a�ciwo�ci:
- miniaturki,
- slideshow,
- wy�wietlanie pe�noekranowe,
- odtwarzanie film�w.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-xine

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}

%{__make} DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{_datadir}/gnome/apps/* $RPM_BUILD_ROOT%{_applnkdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Graphics/*.desktop
%{_pixmapsdir}/*.png
