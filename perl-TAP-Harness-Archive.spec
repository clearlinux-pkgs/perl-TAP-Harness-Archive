#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-TAP-Harness-Archive
Version  : 0.18
Release  : 39
URL      : http://search.cpan.org/CPAN/authors/id/S/SC/SCHWIGON/TAP-Harness-Archive-0.18.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/S/SC/SCHWIGON/TAP-Harness-Archive-0.18.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-TAP-Harness-Archive-perl = %{version}-%{release}
Requires: perl(YAML::Tiny)
BuildRequires : buildreq-cpan
BuildRequires : perl(YAML::Tiny)

%description
No detailed description available

%package dev
Summary: dev components for the perl-TAP-Harness-Archive package.
Group: Development
Provides: perl-TAP-Harness-Archive-devel = %{version}-%{release}
Requires: perl-TAP-Harness-Archive = %{version}-%{release}

%description dev
dev components for the perl-TAP-Harness-Archive package.


%package perl
Summary: perl components for the perl-TAP-Harness-Archive package.
Group: Default
Requires: perl-TAP-Harness-Archive = %{version}-%{release}

%description perl
perl components for the perl-TAP-Harness-Archive package.


%prep
%setup -q -n TAP-Harness-Archive-0.18
cd %{_builddir}/TAP-Harness-Archive-0.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/TAP::Harness::Archive.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
