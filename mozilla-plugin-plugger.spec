Summary:	Mozilla multimedia plugin
Summary(es):	Streaming Netscape Plugin
Summary(pl):	Wtyczka Mozilli do multimediów
Summary(pt_BR):	Plugin para o Netscape para streaming
Name:		mozilla-plugin-plugger
Version:	5.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://fredrik.hubbe.net/plugger/plugger-%{version}.tar.gz
# Source0-md5:	576e32a13955330ee3f7dca3583fcd62
URL:		http://fredrik.hubbe.net/plugger.html
BuildRequires:	mozilla-embedded-devel
Requires:	m4
PreReq:		mozilla-embedded
Obsoletes:	mozilla-plugin-mozplugger
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mozilladir	/usr/%{_lib}/mozilla

%description
Plugger is a plugin which can show many types of multimedia inside
your Netscape or Mozilla-based browser (mozilla itself, galeon,
skipstone, light). To accomplish this, Plugger uses external programs
such as xanim, mtv, timidity and tracker.

%description -l es
Streaming Multimedia plugin for UNIX Netscape.

%description -l pl
Pakiet zawiera wtyczkê, która pozwala na wy¶wietlanie wielu rodzajów
multimediów wewn±trz Netscape lub przegl±darki bazuj±cej na Mozilli
(mozilli jako takiej, galeona, skipstone'a, lighta). Aby to uzyskaæ,
Plugger u¿ywa zewnêtrznych programów, takich jak xanim, mtv, timidity
czy tracker.

%description -l pt_BR
Plugin para o Netscape para streaming.

%prep
%setup -q -n plugger-%{version}

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{mozilladir}/plugins,%{_bindir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man7,%{_sysconfdir}}
install *.so $RPM_BUILD_ROOT%{mozilladir}/plugins
install pluggerrc $RPM_BUILD_ROOT%{_sysconfdir}
install plugger-%{version} $RPM_BUILD_ROOT%{_bindir}
install plugger-controller $RPM_BUILD_ROOT%{_bindir}
install plugger-oohelper $RPM_BUILD_ROOT%{_bindir}
install *.7 $RPM_BUILD_ROOT%{_mandir}/man7
ln -sf pluggerrc $RPM_BUILD_ROOT%{_sysconfdir}/pluggerrc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{mozilladir}/plugins/*.so
%{_mandir}/*/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pluggerrc
%{_sysconfdir}/pluggerrc-*
