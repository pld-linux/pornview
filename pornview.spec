#
# Conditional build:
%bcond_with	gtk2	# use GTK+2 instead of 1.2 (broken)
%bcond_without	xine	# XINE support for movies
#
Summary:	JPEG file viewer
Summary(pl.UTF-8):	Przeglądarka plików JPEG
Name:		pornview
Version:	0.2.0
Release:	0.pre1.4
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/pornview/%{name}-%{version}pre1.tar.gz
# Source0-md5:	339fde6d7ff0cc1053abe951601373e6
Patch0:		%{name}-no_libcharset.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-asneeded.patch
URL:		http://pornview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_xine:BuildRequires:	xine-lib-devel >= 1.0.0}
BuildRequires:	xorg-lib-libXinerama-devel
%if %{with gtk2}
BuildRequires:	gtk+2-devel >= 1:2.0.0
%else
BuildRequires:	gdk-pixbuf-devel >= 0.16.0
BuildRequires:	gtk+-devel >= 1.2.10
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PornView is a JPEG file viewer. Basic features:
- thumbnails,
- slideshow,
- fullscreen,
- support movies.

%description -l pl.UTF-8
PornView jest przeglądarką plików JPEG. Podstawowe właściwości:
- miniaturki,
- slideshow,
- wyświetlanie pełnoekranowe,
- odtwarzanie filmów.

%prep
%setup -q -n %{name}-%{version}pre1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if %{with gtk2}
cat >> acinclude.m4 <<'EOF'
AC_DEFUN([AM_PATH_GTK],[$3])
AC_DEFUN([AM_PATH_GDK_PIXBUF],[$3])
EOF
%endif

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_xine:--enable-xine} \
	%{?with_gtk2:--with-gtk2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/pornview
%{_datadir}/%{name}
%{_desktopdir}/pornview.desktop
%{_pixmapsdir}/pornview.png
