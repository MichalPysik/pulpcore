%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global oldversion 1.1.3

Name:			python-oauth2
Summary:		Python support for improved oauth
Version:		1.2.1
Release:		1%{?dist}
License:		MIT
Group:			System Environment/Libraries
Source0:		http://pypi.python.org/packages/source/o/oauth2/oauth2-%{oldversion}.tar.gz
# Upstream can't seem to manage to put out newer tarballs, just newer git tagged revisions.
Patch0:			python-oauth2-1.1.3-1.2.1.patch
URL:			http://pypi.python.org/pypi/oauth2/
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch
BuildRequires:		python-devel, python-setuptools, python-simplejson
Requires:		python-simplejson

%description
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.

%prep
%setup -q -n oauth2-%{oldversion}
%patch0 -p1 -b .121

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%check
# Tests require mox, not in Fedora yet. 
# export PYTHONPATH=$RPM_BUILD_ROOT/%%{python_sitelib}
# %%{__python} setup.py test

%files
%defattr(-,root,root,-)
%doc README.md LICENSE.txt PKG-INFO
%{python_sitelib}/oauth2/
%{python_sitelib}/oauth2-%{version}-*.egg-info/

%changelog
* Tue Jan 11 2011 Mike McCune <mmccune@redhat.com> 1.2.1-1
- new package built with tito

* Fri Oct 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.1-1
- Initial package for Fedora
