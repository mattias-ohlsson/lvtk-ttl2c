%global debug_package %{nil}

%global commit b64e425f38399a0d18d1252694d6d6980c800841
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lvtk-ttl2c
Version:        1.0.1
Release:        1.git.%{?shortcommit}%{?dist}
Summary:        Turtle to header conversion utility

License:        GPLv3
URL:            https://github.com/lvtk/ttl2c
Source0:        https://github.com/lvtk/ttl2c/archive/%{commit}/ttl2c-%{shortcommit}.tar.gz

BuildRequires:  python3 gcc gcc-c++ boost-devel

%description
Turtle to header conversion utility for LV2 Plugin developers.

%prep
%autosetup -n ttl2c-%{commit}

%build
python3 waf configure --prefix="%{buildroot}%{_prefix}"
python3 waf

%install
rm -rf $RPM_BUILD_ROOT
python3 waf install

%files
%license LICENSE
%{_bindir}/ttl2c

%changelog
* Fri Jun  5 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.0.1-1
- Initial build
