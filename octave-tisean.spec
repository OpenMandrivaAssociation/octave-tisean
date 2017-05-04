%define octpkg tisean

# fix debuginfo-without-sources
%define debug_package %{nil}

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Port of TISEAN 3.0.1 for Octave
Name:		octave-%{octpkg}
Version:	0.2.3
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:		%{name}-0.2.3-fortran.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	gcc-gfortran

Requires:	octave(api) = %{octave_api}
Requires:	octave-signal >= 1.3.0

Requires(post): octave
Requires(postun): octave

%description
Port of TISEAN 3.0.1 for Octave

This package is part of external Octave-Forge collection.

%prep
%setup -q -c %{octpkg}-%{version}
cp %SOURCE0 .

# Apply patch
%patch0 -p0

%build
export CXXFLAGS=" -lgfortran"
%octave_pkg_build #-T

%install
export CXXFLAGS=" -lgfortran"
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

