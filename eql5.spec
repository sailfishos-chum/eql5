Name:           eql5
Version:        20.7.1
Release:        2%{?dist}
Summary:        Qt5 bindings for lisp using ecl

License:        MIT
URL:            https://git.casenave.fr/raz/eql5.git
#Source0:        https://git.casenave.fr/raz/eql5/repository/archive.tar.gz?ref=0acfa4f1fe00e992b0cb8275f999a032b0d7832d
Source:        %{name}-%{version}.tgz

BuildRequires:  ecl = 21.2.1
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qttools-qtuitools-devel
BuildRequires:  qt5-qttools-qthelp-devel
BuildRequires:  libqtwebkit5-devel
BuildRequires:  libqtwebkit5-widgets-devel
Requires:       ecl = 21.2.1
Requires:       gcc-c++
Requires:       readline
Requires:       qt5-qtcore
Requires:       qt5-qtprintsupport
Requires:       qt5-qtmultimedia
Requires:       qt5-qtsql
Requires:       qt5-qtdeclarative-qtquick
Requires:       qt5-qttools-qtuitools
Requires:       qt5-qttools-qthelp
Requires:       libqtwebkit5
Requires:       libqtwebkit5-widgets
Requires(post): coreutils
Requires(postun): coreutils

%description
EQL5 is a framework to use Qt5 with common-lisp using ecl

# no -devel package for header files is split off
# since they are required by the main package


%prep
%setup -q

%build
cd src
ecl -shell make.lisp &&
qmake eql5.pro &&
make INSTALL_ROOT=$RPM_BUILD_ROOT

%install
cd src
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_bindir}/eql5
%{_libdir}/libeql5*
%{_includedir}/eql5/*
%doc examples
%license LICENSE-1.MIT LICENSE-2-MAKE-QIMAGE.txt

%changelog
* Sun Dec 13 2020 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- Adapt for 20.7.1 release

* Mon Oct 21 2019 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- Adapt for 19.9.1 release
- Remove libs compilation

* Mon Feb 11 2019 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- New upstream release

* Sun Dec 31 2017 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- Fix missing wrappers and lib files

* Sat Jun 3 2017 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- Merge upstream and use upstream version number scheme

* Sat Apr 15 2017 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- First release for sailfishos
