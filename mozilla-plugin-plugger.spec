Summary:	Mozilla multimedia plugin
Summary(pl):	Wtyczka Mozilli do multimediów
Name:		mozilla-plugin-plugger
Version:	4.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://fredrik.hubbe.net/plugger/plugger-%{version}-linux-x86-glibc.tar.gz
URL:		http://fredrik.hubbe.net/plugger.html
Prereq:		mozilla-embedded
ExclusiveArch:	%{ix86}
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This package contains flash plugin for Mozilla based browsers, i.e.
mozilla itself, galeon or skipstone.

%description -l pl
Pakiet zawiera plugin dla technologii Flash dla przegl±darek opartych
na Mozilli, np.: mozilli jako takiej, galeona czy te¿ skipstone'a.

%prep
%setup -q -n plugger-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mozilla/plugins,%{_bindir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man7,%{_sysconfdir}}
install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install pluggerrc $RPM_BUILD_ROOT%{_sysconfdir}
install plugger-%{version} $RPM_BUILD_ROOT%{_bindir}
install *.7 $RPM_BUILD_ROOT%{_mandir}/man7
ln -s pluggerrc $RPM_BUILD_ROOT%{_sysconfdir}/pluggerrc-%{version}
gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_mandir}/*/*
%config %{_sysconfdir}/pluggerrc
%{_sysconfdir}/pluggerrc-*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/mozilla/plugins/*.so
