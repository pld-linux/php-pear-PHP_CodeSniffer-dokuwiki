%define		ruleset	dokuwiki
%define		reldate	2009-12-25
%define		ver	%(echo %{reldate} | tr -d -)
Summary:	PHP_CodeSniffer tests for DokuWiki
Name:		php-pear-PHP_CodeSniffer-%{ruleset}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://github.com/splitbrain/dokuwiki/tarball/release_stable_%{reldate}
# Source0-md5:	27c6b35a62c4b508623f4b8eed6d3d58
URL:		http://github.com/splitbrain/dokuwiki/tree/master/_cs/
Requires:	php-pear-PHP_CodeSniffer-dokuwiki
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ruledir	  %{php_pear_dir}/PHP/CodeSniffer/Standards/DokuWiki

%description
Coding Standard tests to be used with PHP CodeSniffer on DokuWiki's
code.

Set DokuWiki to be the default standard:

#> phpcs --config-set default_standard DokuWiki

%prep
%setup -qc
mv *-%{ruleset}-*/_cs/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruledir}
cp -a DokuWiki/* $RPM_BUILD_ROOT%{ruledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruledir}
