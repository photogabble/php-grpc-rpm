%global pecl_name	 grpc
%global ini_name	 40-%{pecl_name}.ini
%global upstream_version 1.62.0
%global upstream_prever  
%global sources		 %{pecl_name}-{%upstream_version}%{?upstream_prever}

Name:		php82-pecl-%{pecl_name}
Version:	%{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:	1%{?dist}.8.2
License:        Apache-2.0
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

BuildRequires:  make
BuildRequires:  gcc >= 7.0
BuildRequires:  gcc-c++
BuildRequires:  php-devel >= 7.0
BuildRequires:  php-pear
BuildRequires:  zlib-devel

%description
Remote Procedure Calls (RPCs) provide a useful abstraction for building
distributed applications and services. The libraries in this repository
provide a concrete implementation of the gRPC protocol, layered over HTTP/2.
These libraries enable communication between clients and servers using
any combination of the supported languages

Package built for PHP  8.2

%prep
%setup -q -c

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable "%{summary}" extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}
phpize
./configure
make

%install
make install INSTALL_ROOT=%{buildroot}
