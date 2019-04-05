Name:           chello
Version:        1.0
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        GPLv3+
URL:            https://github.com/oanhltko/%{name}
Source0:        https://github.com/oanhltko/%{name}/blob/master/%{name}-%{version}.tar.gz


BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  bash 

%description
The long-tail description for our Hello World Example implemented in C.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install

%make_install


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Thu Apr 04 2019 Developer<example@gmail.com> - 1.0-1
- First cello package
