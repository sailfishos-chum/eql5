Name:           eql5
Version:        1.0
Release:        1%{?dist}
Summary:        Qt5 bindings for lisp using ecl

License:        MIT
URL:            https://git.casenave.fr/raz/eql5.git
Source0:        https://git.casenave.fr/raz/eql5/repository/archive.tar.gz?ref=0acfa4f1fe00e992b0cb8275f999a032b0d7832d

BuildRequires:  ecl
BuildRequires:  readline-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  qt5-qttools-qtuitools-devel
BuildRequires:  qt5-qttools-qthelp-devel
Requires:       ecl
Requires:       readline
Requires:       qt5-qtprintsupport
Requires:       qt5-qttools-qtuitools
Requires:       qt5-qttools-qthelp
Requires(post): coreutils
Requires(postun): coreutils

%description
EQL5 is a framework to use Qt5 with common-lisp using ecl

# no -devel package for header files is split off
# since they are required by the main package


%prep
%setup -q

%build
cd src/lisp
ecl -compile ecl-readline.lisp
cd ..

ecl -shell make-eql-lib.lisp &&
qmake eql_lib.pro &&
make &&
qmake eql_exe.pro &&
make &&
LD_LIBRARY_PATH=../ ../eql5 -platform minimal make-eql-lib-wrappers.lisp &&
touch tmp/eql.o &&
qmake eql_lib.pro &&
make &&
qmake module_help.pro &&
make &&
qmake module_network.pro &&
make &&
qmake module_quick.pro &&
make &&
qmake module_sql.pro &&
make &&
qmake module_svg.pro &&
make &&
cd ..

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_bindir}
install libeql5* $RPM_BUILD_ROOT%{_libdir}
install eql5 $RPM_BUILD_ROOT%{_bindir}

%post
/sbin/ldconfig
 
%postun
/sbin/ldconfig

%files
%{_bindir}/eql5
%{_libdir}/libeql5*
%doc LICENSE-1.MIT LICENSE-2-MAKE-QIMAGE.txt

%changelog
* Sat Apr 15 2017 Renaud Casenave-Péré <renaud@casenave-pere.fr>
- First release for sailfishos
