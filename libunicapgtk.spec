%define major	2
%define libname	%mklibname unicapgtk %{major}
%define devname	%mklibname -d unicapgtk

Summary:	Library to build graphical widgets for the unicap library
Name:		libunicapgtk
Version:	0.9.8
Release:	12
License:	GPLv2+
Group:		System/Libraries
Url:		https://www.unicap-imaging.org/
Source0:	http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0:		libunicapgtk-0.9.8-link.patch
Patch1:		libunicapgtk-bz532289.patch
Patch2:		libunicapgtk-0.9.8-destroycb.patch
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libunicap)
BuildRequires:	pkgconfig(libucil)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xv)

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
Building applications with a graphical user interface is made especially
easy with the unicapGTK widget set.

%package	i18n
Summary:	Language files for %{name}
Group:		System/Internationalization 
BuildArch:	noarch
Obsoletes:	libunicapgtk < 0.9.8-4

%description	i18n
This package includes the translation files for %{name}.

%package -n %{libname}
Summary:	Dynamic libraries for Unicapgtk
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}
Conflicts:	%{_lib}unicap2 < 0.9.12-2

%description -n %{libname}
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
Building applications with a graphical user interface is made especially
easy with the unicapGTK widget set.

%package -n %{devname}
Summary:	Development library, include files for Unicapgtk
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development library and headers file
needed in order to develop applications using unicap.

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x --disable-static
%make LIBS="-pthread"

%install
%makeinstall_std
%find_lang unicapgtk

%files i18n -f unicapgtk.lang

%files -n %{libname}
%{_libdir}/libunicapgtk.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/libunicapgtk
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

