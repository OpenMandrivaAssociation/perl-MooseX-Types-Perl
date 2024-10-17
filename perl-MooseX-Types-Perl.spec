%define upstream_name    MooseX-Types-Perl%define upstream_version 0.101343

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Moose types that check against Perl syntax

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Implementation)
BuildRequires:  perl(namespace::autoclean)

BuildArch:	noarch

%description
This library provides MooseX::Types for checking things (mostly strings)
against syntax that is, or is a reasonable subset of, Perl syntax.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*


