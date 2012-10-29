%define	major	20
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	GNU Pth - GNU Portable Threads
Name:		pth
Version:	2.0.7
Release:	11
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gnu.org/software/pth/
Source0:	ftp://ftp.gnu.org/pub/gnu/pth/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/pth/%{name}-%{version}.tar.gz.sig
Patch0:		%{name}-2.0.0-pth-config.in.patch
Patch1:		pth-2.0.7-linux3.patch

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

%package -n	%{libname}
Summary:	GNU Pth - GNU Portable Threads
Group:		System/Libraries

%description -n %{libname}
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

This package provides the main %{name} library.

%package -n	%{devname}
Summary:	GNU Pth - GNU Portable Threads (Headers and Static Libs)
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name} 20 -d
Provides:	%mklibname %{name} 20 -d

%description -n	%{devname}
Pth is a very portable POSIX/ANSI-C based library for Unix platforms.

This package provides all necessary files to develop or compile any
applications or libraries that use %{name} library.

%prep
%setup -q
%patch0 -p1 -b .cflags-ldflags~
%patch1 -p1 -b .linux3~

%build
%configure2_5x	--enable-optimize=yes \
		--enable-pthread=no
	
# (tpg)	without this parallel make fails
%make pth_p.h
%make

%check 
make test

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/pth-config

%files -n %{libname}
%{_libdir}/libpth.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS PORTING README THANKS
%{_bindir}/pth-config
%{multiarch_bindir}/pth-config
%{_datadir}/aclocal/pth.m4
%{_includedir}/pth.h
%{_libdir}/libpth.a
%{_libdir}/libpth.so
%{_mandir}/man?/*
