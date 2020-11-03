#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : geocam-v4l2
Version  : abe533603f2663b8a91be32917fc179f0ce17a26
Release  : 2
URL      : https://github.com/digitalloggers/geocam-v4l2/archive/abe533603f2663b8a91be32917fc179f0ce17a26.tar.gz
Source0  : https://github.com/digitalloggers/geocam-v4l2/archive/abe533603f2663b8a91be32917fc179f0ce17a26.tar.gz
Summary  : MDG-217 camera assembly stream format userspace parser V4L2 plugin
Group    : Development/Tools
License  : LGPL-2.1
Requires: geocam-v4l2-lib = %{version}-%{release}
Requires: geocam-v4l2-license = %{version}-%{release}
BuildRequires : pkgconfig(libv4l2)

%description
# MDG-217 camera assembly stream format userspace parser V4L2 plugin
May be used with an unpatched kernel, or with a kernel patched with the [UVC kernel patch](https://github.com/digitalloggers/geocam-uvc). Additionally, [configuration binaries](https://github.com/digitalloggers/geocam-bin) are required.

%package lib
Summary: lib components for the geocam-v4l2 package.
Group: Libraries
Requires: geocam-v4l2-license = %{version}-%{release}

%description lib
lib components for the geocam-v4l2 package.


%package license
Summary: license components for the geocam-v4l2 package.
Group: Default

%description license
license components for the geocam-v4l2 package.


%prep
%setup -q -n geocam-v4l2-abe533603f2663b8a91be32917fc179f0ce17a26
cd %{_builddir}/geocam-v4l2-abe533603f2663b8a91be32917fc179f0ce17a26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604363032
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604363032
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/geocam-v4l2
cp %{_builddir}/geocam-v4l2-abe533603f2663b8a91be32917fc179f0ce17a26/COPYING.lib %{buildroot}/usr/share/package-licenses/geocam-v4l2/bc667f27fc254baf99c2b974155ba528359ecc43
:
## install_append content
mkdir -p %{buildroot}/usr/lib64/libv4l/plugins
install libv4l_geocam.so %{buildroot}/usr/lib64/libv4l/plugins/
## install_append end

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libv4l/plugins/libv4l_geocam.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/geocam-v4l2/bc667f27fc254baf99c2b974155ba528359ecc43
