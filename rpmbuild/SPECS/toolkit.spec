%define __opt   /opt


Name:		toolkit
Version:	1
Release:	0%{?dist}
Summary:	This is a set of scripts to help in Cloud Operations.

Group:		Applications/Tools
License:	Free
URL:		NA
Source0:	toolkit-1.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
This is a set of scripts to help in Cloud Operations.


%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{__opt}
%{__cp} -rp %{_builddir}/%{name}-%{version}/ %{buildroot}%{__opt}/
%{__ln_s} %{__opt}/%{name}-%{version} %{buildroot}%{__opt}/%{name}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{__opt}/*



%changelog

