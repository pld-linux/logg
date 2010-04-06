# TODO:
# - binary files play_ogg and stream_ogg don't work properly - check it

Summary:	Library for playing Ogg/Vorbis audio files
Summary(pl.UTF-8):	Biblioteka do odtwarzania plików dźwiękowych Ogg/Vorbis
Name:		logg
Version:	2.8
Release:	0.1
License:	MIT
Group:		Development/Tools
Source0:	http://trent.gamblin.ca/logg/%{name}-%{version}.zip
# Source0-md5:	a940e7894f2a487f26ff7d012d06967b
Patch0:		%{name}-Makefile.patch
URL:		http://trent.gamblin.ca/logg/
BuildRequires:	allegro-devel >= 4.4.0
BuildRequires:	libvorbis-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LOGG is an Allegro add-on library for playing Ogg/Vorbis audio files.
It can load Ogg/Vorbis files as Allegro SAMPLEs, or it can stream them
from disk to save memory.

%description -l pl.UTF-8
LOGG jest dodatkową biblioteką do odtwarzania plików dźwiękowych
Ogg/Vorbis. Potrafi ona wczytywać pliki Ogg/Vorbis jako SAMPLE Allegro
lub przesyłać je strumieniem z dysku w celu zaoszczędzenia pamięci.

%package devel
Summary:	Header files for LOGG
Summary(pl.UTF-8):	Pliki nagłówkowe LOGG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	allegro-devel
Requires:	libstdc++-devel
Requires:	libvorbis-devel

%description devel
Header files for LOGG.

%description devel -l pl.UTF-8
Pliki nagłówkowe LOGG.

%package static
Summary:	logg static library
Summary(pl.UTF-8):	Biblioteka statyczna LOGG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
LOGG static library.

%description static -l pl.UTF-8
Biblioteka statyczna LOGG.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -j1 -f Makefile.unix \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__cc} %{rpmcflags} -fPIC -c logg.c
%{__cc} -shared %{rpmldflags} %{rpmcflags} -o liblogg.so logg.o -lvorbisfile `allegro-config --libs`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

%{__make} -f Makefile.unix install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR="%{_libdir}"

install *_ogg $RPM_BUILD_ROOT%{_bindir}
install liblogg.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblogg.so
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/logg.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liblogg.a
