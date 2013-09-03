%define __opt   /opt

Name:           apache-tomcat
Version:        6.0.37
Release:        1%{?dist}
Summary:        Open source software implementation of the Java Servlet and JavaServer Pages technologies

Group:          Applications/Engineering
License:        GPL
URL:            http://tomcat.apache.org
Source0:        apache-tomcat-6.0.37.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:
#Requires:  java

%description
This tomcat version is used by the Opsource Cloud Billing and Payment product.

%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{__opt}
%{__cp} -rp %{_builddir}/apache-tomcat-6.0.37/ %{buildroot}%{__opt}/
%{__ln_s} %{__opt}/%{name}-%{version} %{buildroot}%{__opt}/%{name}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{__opt}/*


%changelog
* Tue Sep 3 2013 Atul Tyagi <atyagi@opsource.net> - 6.0.37-1%{?dist}
- Inital spec created
- TODO include init script.
- TODO include dependency on jdk-1.7u21

