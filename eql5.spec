Name:           eql5
Version:        17.5.1
Release:        1%{?dist}
Summary:        Qt5 bindings for lisp using ecl

License:        MIT
URL:            https://git.casenave.fr/raz/eql5.git
#Source0:        https://git.casenave.fr/raz/eql5/repository/archive.tar.gz?ref=0acfa4f1fe00e992b0cb8275f999a032b0d7832d
Source:        eql5-17.5.1.tar.bz2

BuildRequires:  ecl
BuildRequires:  readline-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  qt5-qttools-qtuitools-devel
BuildRequires:  qt5-qttools-qthelp-devel
BuildRequires:  qt5-qtsvg-devel
Requires:       ecl
Requires:       readline
Requires:       qt5-qtprintsupport
Requires:       qt5-qttools-qtuitools
Requires:       qt5-qttools-qthelp
Requires:       qt5-qtsvg
Requires(post): coreutils
Requires(postun): coreutils

%description
EQL5 is a framework to use Qt5 with common-lisp using ecl

# no -devel package for header files is split off
# since they are required by the main package


%prep
%setup -q

%build
cd lib
ecl -compile ecl-readline.lisp
cd ../src

ecl -shell make.lisp &&
qmake eql5.pro &&
make INSTALL_ROOT=$RPM_BUILD_ROOT &&

LD_LIBRARY_PATH=../ ../eql5 -platform minimal make-wrappers.lisp &&
touch tmp/eql.o &&
qmake eql5.pro &&
make INSTALL_ROOT=$RPM_BUILD_ROOT &&
cd ..

%install
cd src
make install INSTALL_ROOT=$RPM_BUILD_ROOT
cd ..

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_bindir}/eql5
%{_libdir}/libeql5*
%{_includedir}/eql5/*
%doc LICENSE-1.MIT LICENSE-2-MAKE-QIMAGE.txt

%changelog
* Sat Jun 3 2017 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- Merge upstream and use upstream version number scheme

* Sat Apr 15 2017 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- First release for sailfishos
