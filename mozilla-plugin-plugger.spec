Summary:	Mozilla multimedia plugin
Summary(pl):	Wtyczka Mozilli do multimediów
Name:		mozilla-plugin-plugger
Version:	4.0
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://fredrik.hubbe.net/plugger/plugger-%{version}.tar.gz
Source1:	%{name}-npunix.c
Patch0:		%{name}-instance.patch
URL:		http://fredrik.hubbe.net/plugger.html
Prereq:		mozilla-embedded
BuildRequires:	mozilla-embedded-devel
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
%patch0 -p1
mkdir common
cp -f %{SOURCE1} common/npunix.c

%build
CF="%{rpmcflags} -fpic -I%{_includedir}/mozilla"
CF="$CF -I%{_includedir}/mozilla/java -I/usr/include/nspr -I%{_includedir}/mozilla/plugin"
%{__make} all \
        XCFLAGS="$CF" NORM_CFLAGS="$CF" \
        XLDFLAGS=-shared \
        CC=%{__cc} LD=%{__cc} \
        SDK=. X11=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mozilla/plugins,%{_bindir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man7,%{_sysconfdir}}
install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install pluggerrc $RPM_BUILD_ROOT%{_sysconfdir}
install plugger-%{version} $RPM_BUILD_ROOT%{_bindir}
install *.7 $RPM_BUILD_ROOT%{_mandir}/man7
ln -sf pluggerrc $RPM_BUILD_ROOT%{_sysconfdir}/pluggerrc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_mandir}/*/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pluggerrc
%{_sysconfdir}/pluggerrc-*
