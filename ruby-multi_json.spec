%define	pkgname	multi_json
Summary:	A gem to provide swappable JSON backends
Name:		ruby-%{pkgname}
Version:	1.7.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	81c7d5c1024177543cca2e6bffb6aa80
URL:		http://github.com/intridea/multi_json
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-rubygems >= 1.3.6
# http://rubygems.org/gems/gson
#Suggests:	ruby-gson
# http://rubygems.org/gems/json
#Suggests:	ruby-json
# http://rubygems.org/gems/oj
#Suggests:	ruby-oj
Suggests:	ruby-yajl
# https://fedorahosted.org/fpc/ticket/113
Provides:	bundled(okjson) = 20110719
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A gem to provide easy switching between different JSON backends,
including Oj, Yajl, the JSON gem (with C-extensions), the pure-Ruby
JSON gem, and OkJson.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md CONTRIBUTING.md LICENSE.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
