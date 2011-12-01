%define lib_major	2
%define lib_name	%mklibname unicapgtk %{lib_major}
%define develname	%mklibname -d unicapgtk

Summary: Library to build graphical widgets for the unicap library
Name: libunicapgtk
Version: 0.9.8
Release: %mkrel 1
Source0: http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0: libunicapgtk-0.9.8-link.patch
Patch1: libunicapgtk-bz532289.patch
Patch2:	libunicapgtk-0.9.8-destroycb.patch
License: GPLv2+
Group: System/Libraries
Url: http://www.unicap-imaging.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gtk+2-devel
BuildRequires: libunicap-devel
BuildRequires: libucil-devel
BuildRequires: libx11-devel
BuildRequires: libxext-devel
BuildRequires: libxv-devel
BuildRequires: gtk-doc
BuildRequires: intltool

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
Building applications with a graphical user interface is made especially
easy with the unicapGTK widget set.

%package -n %{lib_name}
Summary:	Dynamic libraries for Unicapgtk
Group:		System/Libraries
Requires:	%{name} = %{version}
Conflicts:	%{_lib}unicap2 < 0.9.12

%description -n %{lib_name}
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
Building applications with a graphical user interface is made especially
easy with the unicapGTK widget set.

%package -n %{develname}
Summary:	Static libraries, include files for Unicapgtk
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Conflicts:	%{_lib}unicap-devel < 0.9.12

%description -n %{develname}
Static library and headers file
needed in order to develop applications using unicap.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang unicapgtk

%clean
rm -rf %{buildroot}

%files -f unicapgtk.lang

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/libunicapgtk
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.la
