%define major	20
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{major}

Summary:	GNU Pth - GNU Portable Threads
Name:		pth
Version:	2.0.7
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
URL:		http://www.gnu.org/software/pth/
Source0:	ftp://ftp.gnu.org/pub/gnu/pth/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/pth/%{name}-%{version}.tar.gz.sig
Patch1:		%{name}-2.0.0-pth-config.in.patch
Patch2:		%{name}-2.0.0-parallel-make.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.


%package	-n %{libname}
Summary:	GNU Pth - GNU Portable Threads
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

%description	-n %{libname}
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

This package provides the main %{name} library.


%package	-n %{libname}-devel
Summary:	GNU Pth - GNU Portable Threads (Headers and Static Libs)
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description	-n %{libname}-devel
Pth is a very portable POSIX/ANSI-C based library for Unix platforms.

This package provides all necessary files to develop or compile any
applications or libraries that use %{name} library.

%prep
%setup -q
%patch1 -p1 -b .cflags-ldflags
%patch2 -p1 -b .parallel

%build
%configure2_5x --enable-optimize=yes --enable-pthread=no
%make
%check test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%multiarch_binaries  %{buildroot}%{_bindir}/pth-config

%post -n %{libname} -p /sbin/ldconfig
%postun	-n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_libdir}/lib*.so.%{major}*

%files -n %{libname}-devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING README THANKS
%attr(755,root,root) %{_bindir}/pth-config
%multiarch %attr(755,root,root) %{multiarch_bindir}/pth-config
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_mandir}/man?/*


