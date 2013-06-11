Summary:	Canon EOS Camera Movie Record
Name:		eos-movrec
Version:	0.3.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/eos-movrec/%{name}-%{version}_beta-src.tar.bz2
# Source0-md5:	b9652d602e7d67bfac7bd606940f3e90
URL:		http://valexvir.narod.ru/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	cmake
BuildRequires:	libgphoto2-devel >= 2.4.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software writes short movies with your digital DSLR camera Canon
directly to computer. The camera must have LiveView feature to work,
like in Canon EOS 450D for example. The Program has preview, Av, Tv
and WB control.

%prep
%setup -q -n %{name}-%{version}_beta

%build
export CXXFLAGS="%{rpmcflags}"
%{__cmake} . \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tools/enc_x264.sh TODO
%attr(755,root,root) %{_bindir}/eos_movrec
