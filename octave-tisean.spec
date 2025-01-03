%global octpkg tisean

Summary:	Nonlinear Time Series Analysis
Name:		octave-tisean
Version:	0.2.3
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/tisean/
Source0:	https://downloads.sourceforge.net/octave/tisean-%{version}.tar.gz
# (upstream) https://savannah.gnu.org/bugs/index.php?61583
Patch0:		of-tisean-error_state.patch
# https://hg.octave.org/mxe-octave/file/tip/src/of-tisean-1-fixes.patch
Patch1:		of-tisean-1-fixes.patch
# https://hg.octave.org/mxe-octave/file/tip/src/of-tisean-2-error_state.patch
#Patch2:		of-tisean-2-error_state.patch
# https://hg.octave.org/mxe-octave/file/tip/src/of-tisean-3-octave-9-compat.patch
#Patch3:		of-tisean-3-octave-9-compat.patch
Patch3:		of-tisean-3-octave-9-compat-new.patch
Patch4:		octave-tisean-0.2.3-octave-9.patch

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	octave-signal >= 1.3.0
BuildRequires:	gcc-gfortran
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}
Requires:  	octave-signal >= 1.3.0

Requires(post): octave
Requires(postun): octave

%description
Nonlinear Time Series Analysis. Port of TISEAN 3.0.1.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

