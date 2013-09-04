%define __opt   /opt
%define __user_tomcat	tomcat
%define __group_tomcat	tomcat
%define __init_dir	/etc/init.d

Name:           apache-tomcat
Version:        6.0.37
Release:        2%{?dist}
Summary:        Open source software implementation of the Java Servlet and JavaServer Pages technologies

Group:          Applications/Engineering
License:        GPL
URL:            http://tomcat.apache.org
Source0:        apache-tomcat-6.0.37.tar.gz
Source1:	apache-tomcat.init
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies. 
The Java Servlet and JavaServer Pages specifications are developed under the Java Community Process.

%prep
%setup -q

%pre
/usr/bin/getent group %{__user_tomcat} || /usr/sbin/groupadd -r %{__user_tomcat}
/usr/bin/getent passwd %{__user_tomcat} || /usr/sbin/useradd -r -d %{__opt}/%{name} -s /bin/bash -g %{__group_tomcat} %{__user_tomcat}


%install
rm -rf %{buildroot}
%{__install} -d -m 0755 %{buildroot}%{__init_dir}
mkdir -p %{buildroot}%{__opt}
%{__cp} -rp %{_builddir}/apache-tomcat-6.0.37/ %{buildroot}%{__opt}/
%{__ln_s} %{__opt}/%{name}-%{version} %{buildroot}%{__opt}/%{name}
%{__install} -m 0755 %{SOURCE1} %{buildroot}%{__init_dir}/%{name}

%clean
rm -rf %{buildroot}


%postun
/usr/sbin/userdel tomcat

%files
%defattr(-,tomcat,tomcat,-)
%doc
%{__opt}/*
%attr(0755 root root) %{__init_dir}/apache-tomcat


%changelog
* Wed Sep 4 2013 Atul Tyagi <atyagi@opsource.net> - 6.0.37-2%{?dist}
- Added service account (tomcat) user creation and deletion.
- Added support for init script.

* Tue Sep 3 2013 Atul Tyagi <atyagi@opsource.net> - 6.0.37-1%{?dist}
- Inital spec created

- TODO include dependency on jdk-1.7u21

