%define	major	20
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d
%define _disable_lto 1

Summary:	GNU Pth - GNU Portable Threads
Name:		pth
Version:	2.0.7
Release:	28
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnu.org/software/pth/
Source0:	ftp://ftp.gnu.org/pub/gnu/pth/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/pth/%{name}-%{version}.tar.gz.sig
Source2:	%{name}.rpmlintrc
Patch0:		pth-2.0.0-pth-config.in.patch
Patch1:		pth-2.0.7-linux3.patch
Patch2:		pth-aarch64.patch
Patch3:		pth-2.0.7-select.patch
Patch4:		pth-2.0.7-dont-remove-gcc-g.patch
Patch5:		localedir-configure.patch

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

%description -n	%{devname}
Pth is a very portable POSIX/ANSI-C based library for Unix platforms.

This package provides all necessary files to develop or compile any
applications or libraries that use %{name} library.

%prep
%setup -q
%apply_patches

%build
CFLAGS="%{optflags} -Ofast" \
%configure \
	--enable-optimize=yes \
	--disable-static \
	--enable-pthread=no

# (tpg)	without this parallel make fails
%make pth_p.h
%make

%check
make test

%install
%makeinstall_std
mkdir -p %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/libpth.so.%{major}* %{buildroot}/%{_lib}
ln -srf %{buildroot}/%{_lib}/libpth.so.%{major}.*.* %{buildroot}%{_libdir}/libpth.so

%files -n %{libname}
/%{_lib}/libpth.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS PORTING README THANKS
%{_bindir}/pth-config
%{_datadir}/aclocal/pth.m4
%{_includedir}/pth.h
%{_libdir}/libpth.so
%{_mandir}/man?/*
