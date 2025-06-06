%global octpkg tisean

# For now -- since C code (built with clang) and
# Fortran code (built with gfortran) are linked
# together, LTO object files don't work
%global _disable_lto 1

Summary:	Nonlinear Time Series Analysis
Name:		octave-tisean
Version:	0.2.3
Release:	5
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/tisean/
Source0:	https://downloads.sourceforge.net/octave/tisean-%{version}.tar.gz
# (upstream) https://savannah.gnu.org/bugs/index.php?61583
Patch0:		of-tisean-error_state.patch
# https://hg.octave.org/mxe-octave/file/tip/src/of-tisean-1-fixes.patch
Patch1:		of-tisean-1-fixes.patch
# https://hg.octave.org/mxe-octave/file/tip/src/of-tisean-3-octave-9-compat.patch
Patch3:		of-tisean-3-octave-9-compat.patch
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

