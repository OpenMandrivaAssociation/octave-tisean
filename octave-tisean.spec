%global octpkg tisean

# fix debuginfo-without-sources
#define debug_package %{nil}

Summary:	Port of TISEAN 3.0.1 for Octave
Name:		octave-%{octpkg}
Version:	0.2.3
Release:	1
Url:		https://octave.sourceforge.io/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
#Patch0:		%{name}-0.2.3-fortran.patch
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	gcc-gfortran
BuildRequires:	octave-signal >= 1.3.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-signal >= 1.3.0

Requires(post): octave
Requires(postun): octave

%description
Port of TISEAN 3.0.1 for Octave

This package is part of external Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
export CC=gcc
export CXX=g++
export CXXFLAGS="%{optflags} -lgfortran"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

