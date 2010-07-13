# Required due to circular dependencies in lt_libraries
%define _disable_ld_no_undefined	1

%define name	coin-or
%define major	0
%define libname	%mklibname %{name} %{major}

Epoch:		1

Name:		%{name}
Group:		Sciences/Mathematics
License:	CPL
Summary:	COmputational INfrastructure for Operations Research
Version:	1.3.1
Release:	%mkrel 1
URL:		http://www.coin-or.org/
Source0:	http://www.coin-or.org/download/source/CoinAll/CoinAll-1.3.1.tgz
# wget http://netlib.sandia.gov/cgi-bin/netlib/netlibfiles.tar?filename=netlib/ampl/solvers
Source1:	solvers.tar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	blas-devel
BuildRequires:	glpk-devel
BuildRequires:	lapack-devel
BuildRequires:	readline-devel

Obsoletes:	cbc = 2.4.0
Provides:	cbc = 2.4.0

Patch0:		CoinAll-1.3.1-format.patch

%description
The Computational Infrastructure for Operations Research (COIN-OR**, or
simply COIN) project is an initiative to spur the development of open-source
software for the operations research community.

Why open source? The Open Source Initiative explains it well. When people
can read, redistribute, and modify the source code, software evolves. People
improve it, people adapt it, people fix bugs.  The results of open-source
development have been remarkable. Community-based efforts to develop software
under open-source licenses have produced high-quality, high-performance
code---code on which much of the Internet is run.

Why for OR? Consider the following scenario. You read about an optimization
algorithm in the literature and you get an idea on how to improve it.  Today,
testing your new idea typically requires re-implementing (and re-debugging and
re-testing) the original algorithm.  Often, clever implementation details
aren't published. It can be difficult to replicate reported performance.
Now imagine the scenario if the original algorithm was publicly available
in a community repository. Weeks of re-implementing would no longer be
required. You would simply check out a copy of it for yourself and modify it.
Imagine the productivity gains from software reuse!
Our goal is to create for mathematical software what the open literature is
for mathematical theory.

We are building an open-source community for operations research software in
order to speed development and deployment of models, algorithms, and
cutting-edge computational research, as well as provide a forum for peer
review of software similar to that provided by archival journals for
theoretical research. This is a lofty goal, but we believe it's a worthwhile
one. We have ideas, but we don't have all the answers. Only the community of
users and contributors can define what is needed to make it a reality. For
further information, please see the FAQs page, as well as the COIN-OR
resources page. 

%package	-n %{libname}
Group:		System/Libraries
License:	CPL
Summary:	An open-source mixed integer programming solver
Provides:	lib%{name} = %{version}-%{release}
Obsoletes:	%{mklibname cbc 0} = 2.4.0
Provides:	%{mklibname cbc 0} = 2.4.0

%description	-n %{libname}
The Computational Infrastructure for Operations Research (COIN-OR**, or
simply COIN) project is an initiative to spur the development of open-source
software for the operations research community.

%package	-n lib%{name}-devel
Group:		Development/C
License:	CPL
Summary:	An open-source mixed integer programming solver
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	libcbc-devel = 2.4.0
Provides:	libcbc-devel = 2.4.0

%description	-n lib%{name}-devel
The Computational Infrastructure for Operations Research (COIN-OR**, or
simply COIN) project is an initiative to spur the development of open-source
software for the operations research community.

%prep
%setup -q -n CoinAll-%{version}

pushd ThirdParty/ASL
    tar xf %{SOURCE1}
    gunzip -fr solvers
popd

%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/blis
%{_bindir}/bonmin
%{_bindir}/cbc
%{_bindir}/clp
%{_bindir}/couenne
%{_bindir}/ipopt
%{_bindir}/OSAmplClient
%{_bindir}/OSSolverService
%{_bindir}/symphony

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files		-n lib%{name}-devel
%defattr(-,root,root)
%dir %{_includedir}/coin
%{_includedir}/coin/*
%dir %{_includedir}/cppad
%{_includedir}/cppad/*
%{_libdir}/amplsolver.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%dir %{_docdir}/coin
%{_docdir}/coin/*
