%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	GameServerQuery
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - interface to query a game server
Summary(pl):	%{_pearname} - interfejs do odpytywanie serwera gier
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c1b70ac52031046605522e3df64bb13c
URL:		http://pear.php.net/package/Net_GameServerQuery/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_GameServerQuery is an object for querying game servers.
Currently only supports basic "status" information.
Built in support for over 20 games.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_GameServerQuery to obiekt do odpytywania serwerów gier. Aktualnie
obs³uguje tylko podstawowe informacje o stanie. Ma wbudowan± obs³ugê
ponad 20 gier.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
