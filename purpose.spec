#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : purpose
Version  : 5.103.0
Release  : 56
URL      : https://download.kde.org/stable/frameworks/5.103/purpose-5.103.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.103/purpose-5.103.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.103/purpose-5.103.0.tar.xz.sig
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
BuildRequires : kaccounts-integration-dev
BuildRequires : kio-dev
BuildRequires : kirigami2-dev
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
%setup -q -n purpose-5.103.0
cd %{_builddir}/purpose-5.103.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676321800
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676321800
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/purpose
cp %{_builddir}/purpose-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/purpose/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/purpose-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/purpose/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/purpose-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/purpose/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/purpose-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/purpose/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
pushd clr-build
%make_install
popd
%find_lang libpurpose_quick
%find_lang libpurpose_widgets
%find_lang purpose-fileitemaction
%find_lang purpose_barcode
%find_lang purpose_bluetooth
%find_lang purpose_imgur
%find_lang purpose_kdeconnect
%find_lang purpose_kdeconnectsms
%find_lang purpose_ktp-sendfile
%find_lang purpose_nextcloud
%find_lang purpose_pastebin
%find_lang purpose_phabricator
%find_lang purpose_reviewboard
%find_lang purpose_saveas
%find_lang purpose_youtube

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/purposeprocess

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/phabricator-purpose.png
/usr/share/icons/hicolor/128x128/apps/reviewboard-purpose.png
/usr/share/icons/hicolor/16x16/apps/phabricator-purpose.png
/usr/share/icons/hicolor/16x16/apps/reviewboard-purpose.png
/usr/share/purpose/barcodeplugin_config.qml
/usr/share/purpose/bluetoothplugin_config.qml
/usr/share/purpose/kdeconnectplugin_config.qml
/usr/share/purpose/phabricatorplugin_config.qml
/usr/share/purpose/reviewboardplugin_config.qml
/usr/share/purpose/saveasplugin_config.qml
/usr/share/qlogging-categories5/purpose.categories
/usr/share/qlogging-categories5/purpose.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/purpose/Purpose/AlternativesModel
/usr/include/KF5/purpose/Purpose/Configuration
/usr/include/KF5/purpose/Purpose/Job
/usr/include/KF5/purpose/Purpose/PluginBase
/usr/include/KF5/purpose/purpose/alternativesmodel.h
/usr/include/KF5/purpose/purpose/configuration.h
/usr/include/KF5/purpose/purpose/job.h
/usr/include/KF5/purpose/purpose/pluginbase.h
/usr/include/KF5/purpose/purpose/purpose_export.h
/usr/include/KF5/purpose/purpose_version.h
/usr/include/KF5/purposewidgets/PurposeWidgets/Menu
/usr/include/KF5/purposewidgets/purposewidgets/menu.h
/usr/include/KF5/purposewidgets/purposewidgets/purposewidgets_export.h
/usr/lib64/cmake/KDEExperimentalPurpose/KDEExperimentalPurposeConfig.cmake
/usr/lib64/cmake/KF5Purpose/KF5PurposeConfig.cmake
/usr/lib64/cmake/KF5Purpose/KF5PurposeConfigVersion.cmake
/usr/lib64/cmake/KF5Purpose/KF5PurposeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Purpose/KF5PurposeTargets.cmake
/usr/lib64/libKF5Purpose.so
/usr/lib64/libKF5PurposeWidgets.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Purpose.so.5
/usr/lib64/libKF5Purpose.so.5.103.0
/usr/lib64/libKF5PurposeWidgets.so.5
/usr/lib64/libKF5PurposeWidgets.so.5.103.0
/usr/lib64/libPhabricatorHelpers.so.5
/usr/lib64/libPhabricatorHelpers.so.5.103.0
/usr/lib64/libReviewboardHelpers.so.5
/usr/lib64/libReviewboardHelpers.so.5.103.0
/usr/lib64/qt5/plugins/kf5/kfileitemaction/sharefileitemaction.so
/usr/lib64/qt5/plugins/kf5/purpose/barcodeplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/bluetoothplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/emailplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/imgurplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/kdeconnectplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/kdeconnectsmsplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/ktpsendfileplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/pastebinplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/phabricatorplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/reviewboardplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/saveasplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/telegramplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/twitterplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/AlternativesView.qml
/usr/lib64/qt5/qml/org/kde/purpose/JobView.qml
/usr/lib64/qt5/qml/org/kde/purpose/libpurposequickplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/phabricator/libphabricatorquickplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/phabricator/qmldir
/usr/lib64/qt5/qml/org/kde/purpose/qmldir
/usr/lib64/qt5/qml/org/kde/purpose/reviewboard/librbpurposequickplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/reviewboard/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/purpose/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/purpose/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/purpose/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/purpose/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libpurpose_quick.lang -f libpurpose_widgets.lang -f purpose-fileitemaction.lang -f purpose_barcode.lang -f purpose_bluetooth.lang -f purpose_imgur.lang -f purpose_kdeconnect.lang -f purpose_kdeconnectsms.lang -f purpose_ktp-sendfile.lang -f purpose_nextcloud.lang -f purpose_pastebin.lang -f purpose_phabricator.lang -f purpose_reviewboard.lang -f purpose_saveas.lang -f purpose_youtube.lang
%defattr(-,root,root,-)

