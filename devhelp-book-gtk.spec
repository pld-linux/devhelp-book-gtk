Summary:	DevHelp book: GTK
Summary(pl):	Ksi±¿ka do DevHelp'a o GTK
Name:		devhelp-book-gtk
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gtk-1.2.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about GTK 1.2

%description -l pl
Ksi±¿ka do DevHelp o GTK 1.2

%prep
%setup -q -c gtk-%{version} -n gtk-%{version}

%build
mv -f book gtk-%{version}
mv -f book.devhelp gtk-%{version}.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gtk-%{version}
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gtk-%{version}.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gtk-%{version}/* $RPM_BUILD_ROOT%{_prefix}/books/gtk-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
