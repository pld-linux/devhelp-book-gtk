Summary:	DevHelp book: GTK+ 1.2
Summary(pl.UTF-8):	Książka do DevHelpa o GTK+ 1.2
Name:		devhelp-book-gtk
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gtk-1.2.tar.gz
# Source0-md5:	4ac4d8c15b4c5bc210669fdc0e5d06d3
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about GTK+ 1.2.

%description -l pl.UTF-8
Książka do DevHelpa o GTK+ 1.2.

%prep
%setup -q -c -n gtk-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gtk-%{version},specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gtk-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gtk-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
