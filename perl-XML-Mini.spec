%define upstream_name    XML-Mini
%define upstream_version 1.38

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Perl implementation of the XML::Mini XML create/parse interface
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:        http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
XML::Mini is a set of Perl classes that allow you to access XML data and create
valid XML output with a tree-based hierarchy of elements. The MiniXML API has
both Perl and PHP implementations.

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/Mini.pm
%{perl_vendorlib}/XML/Mini/*.pm
%{perl_vendorlib}/XML/Mini/Element/*.pm
%{_mandir}/man3*/*
