#
# INFO:
#
# don't unhash xine-lib-devel becouse playing movies is still experimential
#
Summary:	jpeg file viewer
Summary(pl):	Przegl±darka jpegów
Name:		pornview
Version:	0.1.1
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://pornview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:  gtk+-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
#BuildRequires:	xine-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix  /usr/X11R6

%description
PornView is a jpeg file viewer. Basic features:
- thumbnails,
- slideshow,
- fullscreen, 

#- support movies.
 
%description -l pl
PornView jest przegl±dark± jpegów. Podstawowe w³a¶ciwo¶ci:
- miniaturki,
- slideshow,
- wy¶wietlanie pe³noekranowe,

#- odtwarzanie filmów.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
#--with-xine

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}

%{__make} DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{_prefix}/share/gnome/apps/* $RPM_BUILD_ROOT%{_applnkdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/*.desktop
%{_pixmapsdir}/*.png
