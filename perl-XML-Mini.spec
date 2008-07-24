%define module  XML-Mini
%define name    perl-%{module}
%define version 1.38
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl implementation of the XML::Mini XML create/parse interface
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
XML::Mini is a set of Perl classes that allow you to access XML data and create
valid XML output with a tree-based hierarchy of elements. The MiniXML API has
both Perl and PHP implementations.

%prep

%setup -q -n %{module}-%{version} 

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

