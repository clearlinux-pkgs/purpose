#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : purpose
Version  : 6.11.0
Release  : 89
URL      : https://download.kde.org/stable/frameworks/6.11/purpose-6.11.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.11/purpose-6.11.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.11/purpose-6.11.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Framework for providing abstractions to get the developer's purposes fulfilled
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: purpose-data = %{version}-%{release}
Requires: purpose-lib = %{version}-%{release}
Requires: purpose-license = %{version}-%{release}
Requires: purpose-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kirigami-dev
BuildRequires : kirigami2-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Purpose
Offers available actions for a specific purpose
## Introduction
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package data
Summary: data components for the purpose package.
Group: Data

%description data
data components for the purpose package.


%package dev
Summary: dev components for the purpose package.
Group: Development
Requires: purpose-lib = %{version}-%{release}
Requires: purpose-data = %{version}-%{release}
Provides: purpose-devel = %{version}-%{release}
Requires: purpose = %{version}-%{release}

%description dev
dev components for the purpose package.


%package lib
Summary: lib components for the purpose package.
Group: Libraries
Requires: purpose-data = %{version}-%{release}
Requires: purpose-license = %{version}-%{release}

%description lib
lib components for the purpose package.


%package license
Summary: license components for the purpose package.
Group: Default

%description license
license components for the purpose package.


%package locales
Summary: locales components for the purpose package.
Group: Default

%description locales
locales components for the purpose package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n purpose-6.11.0
cd %{_builddir}/purpose-6.11.0
pushd ..
cp -a purpose-6.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739580605
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739580605
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/purpose
cp %{_builddir}/purpose-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/purpose/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/purpose-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/purpose/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/purpose-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/purpose/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/purpose-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/purpose/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libpurpose6_quick
%find_lang libpurpose6_widgets
%find_lang purpose6_barcode
%find_lang purpose6_bluetooth
%find_lang purpose6_fileitemaction
%find_lang purpose6_imgur
%find_lang purpose6_kdeconnect
%find_lang purpose6_kdeconnectsms
%find_lang purpose6_nextcloud
%find_lang purpose6_pastebin
%find_lang purpose6_phabricator
%find_lang purpose6_reviewboard
%find_lang purpose6_saveas
%find_lang purpose6_youtube
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/purposeprocess
/usr/lib64/libexec/kf6/purposeprocess

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/phabricator-purpose6.png
/usr/share/icons/hicolor/128x128/apps/reviewboard-purpose6.png
/usr/share/icons/hicolor/16x16/apps/phabricator-purpose6.png
/usr/share/icons/hicolor/16x16/apps/reviewboard-purpose6.png
/usr/share/kf6/purpose/barcodeplugin_config.qml
/usr/share/kf6/purpose/bluetoothplugin_config.qml
/usr/share/kf6/purpose/kdeconnectplugin_config.qml
/usr/share/kf6/purpose/phabricatorplugin_config.qml
/usr/share/kf6/purpose/reviewboardplugin_config.qml
/usr/share/kf6/purpose/saveasplugin_config.qml
/usr/share/qlogging-categories6/purpose.categories
/usr/share/qlogging-categories6/purpose.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/Purpose/Purpose/AlternativesModel
/usr/include/KF6/Purpose/Purpose/Configuration
/usr/include/KF6/Purpose/Purpose/Job
/usr/include/KF6/Purpose/Purpose/PluginBase
/usr/include/KF6/Purpose/purpose/alternativesmodel.h
/usr/include/KF6/Purpose/purpose/configuration.h
/usr/include/KF6/Purpose/purpose/job.h
/usr/include/KF6/Purpose/purpose/pluginbase.h
/usr/include/KF6/Purpose/purpose/purpose_export.h
/usr/include/KF6/Purpose/purpose_version.h
/usr/include/KF6/PurposeWidgets/Purpose/Menu
/usr/include/KF6/PurposeWidgets/purpose/menu.h
/usr/include/KF6/PurposeWidgets/purpose/purposewidgets_export.h
/usr/lib64/cmake/KF6Purpose/KF6PurposeConfig.cmake
/usr/lib64/cmake/KF6Purpose/KF6PurposeConfigVersion.cmake
/usr/lib64/cmake/KF6Purpose/KF6PurposeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Purpose/KF6PurposeTargets.cmake
/usr/lib64/libKF6Purpose.so
/usr/lib64/libKF6PurposeWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Purpose.so.6.11.0
/V3/usr/lib64/libKF6PurposeWidgets.so.6.11.0
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/sharefileitemaction.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/barcodeplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/bluetoothplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/clipboardplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/emailplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/imgurplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/kdeconnectplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/kdeconnectsmsplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/pastebinplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/phabricatorplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/reviewboardplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/saveasplugin.so
/V3/usr/lib64/qt6/plugins/kf6/purpose/telegramplugin.so
/V3/usr/lib64/qt6/qml/org/kde/purpose/kdeconnect/libkdeconnectQml.so
/V3/usr/lib64/qt6/qml/org/kde/purpose/libpurposequickplugin.so
/V3/usr/lib64/qt6/qml/org/kde/purpose/phabricator/libphabricatorquickplugin.so
/V3/usr/lib64/qt6/qml/org/kde/purpose/reviewboard/librbpurposequickplugin.so
/usr/lib64/libKF6Purpose.so.6
/usr/lib64/libKF6Purpose.so.6.11.0
/usr/lib64/libKF6PurposeWidgets.so.6
/usr/lib64/libKF6PurposeWidgets.so.6.11.0
/usr/lib64/qt6/plugins/kf6/kfileitemaction/sharefileitemaction.so
/usr/lib64/qt6/plugins/kf6/purpose/barcodeplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/bluetoothplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/clipboardplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/emailplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/imgurplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/kdeconnectplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/kdeconnectsmsplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/pastebinplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/phabricatorplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/reviewboardplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/saveasplugin.so
/usr/lib64/qt6/plugins/kf6/purpose/telegramplugin.so
/usr/lib64/qt6/qml/org/kde/purpose/AlternativesView.qml
/usr/lib64/qt6/qml/org/kde/purpose/JobView.qml
/usr/lib64/qt6/qml/org/kde/purpose/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/purpose/kdeconnect/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/purpose/kdeconnect/kdeconnectQml.qmltypes
/usr/lib64/qt6/qml/org/kde/purpose/kdeconnect/libkdeconnectQml.so
/usr/lib64/qt6/qml/org/kde/purpose/kdeconnect/qmldir
/usr/lib64/qt6/qml/org/kde/purpose/libpurposequickplugin.so
/usr/lib64/qt6/qml/org/kde/purpose/phabricator/libphabricatorquickplugin.so
/usr/lib64/qt6/qml/org/kde/purpose/phabricator/qmldir
/usr/lib64/qt6/qml/org/kde/purpose/purposequickplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/purpose/qmldir
/usr/lib64/qt6/qml/org/kde/purpose/reviewboard/librbpurposequickplugin.so
/usr/lib64/qt6/qml/org/kde/purpose/reviewboard/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/purpose/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/purpose/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/purpose/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/purpose/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libpurpose6_quick.lang -f libpurpose6_widgets.lang -f purpose6_barcode.lang -f purpose6_bluetooth.lang -f purpose6_fileitemaction.lang -f purpose6_imgur.lang -f purpose6_kdeconnect.lang -f purpose6_kdeconnectsms.lang -f purpose6_nextcloud.lang -f purpose6_pastebin.lang -f purpose6_phabricator.lang -f purpose6_reviewboard.lang -f purpose6_saveas.lang -f purpose6_youtube.lang
%defattr(-,root,root,-)

