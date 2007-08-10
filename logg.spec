# TODO:
# - Generate .so and .la files and add they to the -devel package
# - binary files play_ogg and stream_ogg doesn't work properly - check it

Summary:	Library for playing OGG/Vorbis audio files
Summary(pl.UTF-8):	Biblioteka do odtwarzania plików audio OGG/Vorbis
Name:		logg
Version:	2.5
Release:	0.1
License:	MIT
Group:		Development/Tools
Source0:	http://trent.gamblin.ca/logg/%{name}-%{version}.tar.bz2
# Source0-md5:	43be1e144708f6162b04b7c54e218a67
Patch0:		%{name}-Makefile.patch
URL:		http://trent.gamblin.ca/logg/
BuildRequires:	allegro-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LOGG is an Allegro add-on library for playing OGG/Vorbis audio files.
It can load OGG/Vorbis files as Allegro SAMPLE's, or it can stream
them from disk to save memory.

%description -l pl.UTF-8
LOGG jest dodatkową biblioteką do odtwarzania plików audio
OGG/Vorbis. Potrafi ona wczytywać pliki OGG/Vorbis jako Allegro
SAMPLE's lub strumieniować je z dysku do pamięci.

%package devel
Summary:	Header files for LOGG
Summary(pl.UTF-8):	Pliki nagłówkowe LOGG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	allegro-devel

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
%{__make} -f Makefile.unix \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

%{__make} -f Makefile.unix install \
	DESTDIR=$RPM_BUILD_ROOT

install *_ogg $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/logg.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liblogg.a
