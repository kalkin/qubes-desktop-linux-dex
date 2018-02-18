Name:           dex
Version:        0.8.0
Release:        1%{?dist}
Summary:        Generate and execute DesktopEntry files of the Application type
License:        GPLv3
URL:            https://github.com/jceb/%{name}
Source0:        https://github.com/jceb/%{name}/archive/v%{version}.tar.gz
BuildRequires:	python3-sphinx
Requires:       python3
%description
dex, DesktopEntry Execution, is a program to generate and execute DesktopEntry
files of the Application type.

%if 0%{?qubes_builder}
%define _sourcedir %(pwd)
%endif

%global debug_package %{nil}

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir} DOCPREFIX=%{_defaultdocdir}/dex


%files
%license %{_docdir}/dex/LICENSE
%doc README.rst
%{_bindir}/dex
%{_mandir}/man1/dex.1.gz


%changelog

