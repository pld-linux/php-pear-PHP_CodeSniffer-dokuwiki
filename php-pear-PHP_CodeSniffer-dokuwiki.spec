%define		ruleset	dokuwiki
Summary:	PHP_CodeSniffer tests for DokuWiki
Name:		php-pear-PHP_CodeSniffer-%{ruleset}
Version:	20100129
Release:	2
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://download.github.com/splitbrain-dokuwiki-release_stable_2009-12-25-249-gc275533.tar.gz
# Source0-md5:	8a9f0f6470877422f6aeb00e6513fa58
URL:		http://github.com/splitbrain/dokuwiki/tree/master/_cs/
Requires:	php-pear
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
