Summary:     Compact Disc Digital Audio (CDDA) extraction tool (or ripper)
Name:        cdparanoia
Version:     10.2
Release:     29
License:     GPLv2 and LGPLv2
URL:         http://www.xiph.org/paranoia/index.html
Source:      http://downloads.xiph.org/releases/cdparanoia/cdparanoia-III-%{version}.src.tgz
Patch0000:   cdparanoia-10.2-#463009.patch
Patch0001:   cdparanoia-10.2-endian.patch
Patch0002:   cdparanoia-10.2-install.patch
Patch0003:   cdparanoia-10.2-format-security.patch
Patch0004:   cdparanoia-use-proper-gnu-config-files.patch
Patch0005:   cdparanoia-10.2-ldflags.patch
Provides:    cdparanoia-libs
Obsoletes:   cdparanoia-libs

%description
Cdparanoia (Paranoia III) is a audio CD digital audio extraction application.
It extracts audio from compact discs directly as data, and writes the data to
a file or pipe in WAV, AIFC or raw 16 bit linear PCM format. It also contains
dynamic libraries needed for appliation which read CD Digital Audio disks.

%package     devel
Summary:     Development tools for libcdda_paranoia (Paranoia III)
Requires:    %{name} = %{version}-%{release}
License:     LGPLv2
Provides:    cdparanoia-static
Obsoletes:   cdparanoia-static

%description devel
It provides the static/dynamic libraries and header files needed for developing applications
to read CD-DA.

%package     help
Summary:     Help manual for cdparanoia

%description help
This package provides help manual function for cdparanoia separately.

%prep
%autosetup -n %{name}-III-%{version} -p1
cp /usr/lib/rpm/%{_vendor}/config.* .

%build
%configure --includedir=%{_includedir}/cdda
make OPT="$RPM_OPT_FLAGS -Wno-pointer-sign -Wno-unused" LDFLAGS="%{?__global_ldflags}"

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING* README
%{_bindir}/cdparanoia
%{_libdir}/*.so.*

%files help
%{_mandir}/man1/cdparanoia.1*

%files devel
%{_includedir}/cdda/
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Fri Sep 20 2019 Alex Chao <zhaolei746@huawei.com> - 10.2-29
- Package init
