%define major 5
%define libname %mklibname KPimKDAV %{major}
%define devname %mklibname KPimKDAV -d

Name: kdav
Version:	 18.12.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: DAV implementation for KDE
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(PythonInterp)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)
BuildRequires: cmake(Qt5Test)
Requires: %{libname} = %{EVRD}

%description
DAV implementation for KDE.

%package -n %{libname}
Summary: DAV implementation for KDE
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
DAV support library for KDE.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libkdav

%files -f libkdav.lang
%{_sysconfdir}/xdg/kdav.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
