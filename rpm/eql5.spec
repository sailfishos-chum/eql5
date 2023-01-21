Name:           eql5
Version:        24.2.1
Release:        1%{?dist}
Summary:        Qt5 bindings for lisp using ecl

License:        MIT
URL:            https://git.casenave.fr/raz/eql5.git
Source:        %{name}-%{version}.tgz

BuildRequires:  ecl = 24.5.10
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
Requires:       ecl = 24.5.10
Requires:       gcc-c++
Requires:       readline
Requires:       qt5-qtcore
Requires:       qt5-qtmultimedia
Requires:       qt5-qtsql
Requires:       qt5-qtwidgets
Requires:       qt5-qtdeclarative-qtquick
Requires(post): coreutils
Requires(postun): coreutils

%description
EQL5 is a framework to use Qt5 with common-lisp using ecl

# no -devel package for header files is split off
# since they are required by the main package


%prep
%setup -q -n %{name}-%{version}/EQL5

%build
cd src
ecl -shell make.lisp &&
export SAILFISH=sailfish &&
export EQL_VERSION=%{version} &&
qmake eql5.pro &&
make -j 4 INSTALL_ROOT=$RPM_BUILD_ROOT

%install
cd src
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_bindir}/eql5
%{_libdir}/libeql5.so*
%{_libdir}/libeql5.a
%{_libdir}/libeql5.prl
%{_libdir}/eql5/libeql5_*.so*
%{_includedir}/eql5/*
%doc examples
%license LICENSE-1.MIT LICENSE-2-MAKE-QIMAGE.txt

%changelog
* Sun Jun 29 2025 Renaud Casenave-Péré <renaud@casenave-pere.fr> 24.2.1-1
- New upstream release

* Thu Mar 25 2021 Renaud Casenave-Péré <renaud@casenave-pere.fr> 21.3.4-1
- New upstream release

* Wed Mar 10 2021 Renaud Casenave-Péré <renaud@casenave-pere.fr> 21.3.3-1
- Add static library build step
- New upstream release

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
