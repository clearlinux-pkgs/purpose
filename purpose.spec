#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : purpose
Version  : 5.53.0
Release  : 7
URL      : https://download.kde.org/stable/frameworks/5.53/purpose-5.53.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.53/purpose-5.53.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.53/purpose-5.53.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: purpose-data = %{version}-%{release}
Requires: purpose-lib = %{version}-%{release}
Requires: purpose-license = %{version}-%{release}
Requires: purpose-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n purpose-5.53.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544545181
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1544545181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/purpose
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/purpose/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libpurpose_quick
%find_lang libpurpose_widgets
%find_lang purpose_email
%find_lang purpose_imgur
%find_lang purpose_kdeconnect
%find_lang purpose_ktp-sendfile
%find_lang purpose_nextcloud
%find_lang purpose_pastebin
%find_lang purpose_phabricator
%find_lang purpose_saveas
%find_lang purpose_twitter
%find_lang purpose_youtube
%find_lang purpose_reviewboard
%find_lang purpose-fileitemaction

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/purposeprocess

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/phabricator-purpose.png
/usr/share/icons/hicolor/128x128/apps/reviewboard-purpose.png
/usr/share/icons/hicolor/16x16/apps/phabricator-purpose.png
/usr/share/icons/hicolor/16x16/apps/reviewboard-purpose.png
/usr/share/purpose/bluetoothplugin_config.qml
/usr/share/purpose/kdeconnectplugin_config.qml
/usr/share/purpose/phabricatorplugin_config.qml
/usr/share/purpose/reviewboardplugin_config.qml
/usr/share/purpose/saveasplugin_config.qml
/usr/share/xdg/purpose.categories

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
/usr/lib64/libKF5Purpose.so.5.53.0
/usr/lib64/libKF5PurposeWidgets.so.5
/usr/lib64/libKF5PurposeWidgets.so.5.53.0
/usr/lib64/libPhabricatorHelpers.so.5
/usr/lib64/libPhabricatorHelpers.so.5.53.0
/usr/lib64/libReviewboardHelpers.so.5
/usr/lib64/libReviewboardHelpers.so.5.53.0
/usr/lib64/qt5/plugins/kf5/kfileitemaction/sharefileitemaction.so
/usr/lib64/qt5/plugins/kf5/purpose/bluetoothplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/emailplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/imgurplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/kdeconnectplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/ktpsendfileplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/pastebinplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/phabricatorplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/reviewboardplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/saveasplugin.so
/usr/lib64/qt5/plugins/kf5/purpose/telegramplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/libpurposequickplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/phabricator/libphabricatorquickplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/phabricator/qmldir
/usr/lib64/qt5/qml/org/kde/purpose/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/purpose/qmldir
/usr/lib64/qt5/qml/org/kde/purpose/reviewboard/librbpurposequickplugin.so
/usr/lib64/qt5/qml/org/kde/purpose/reviewboard/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/purpose/COPYING.LIB

%files locales -f libpurpose_quick.lang -f libpurpose_widgets.lang -f purpose_email.lang -f purpose_imgur.lang -f purpose_kdeconnect.lang -f purpose_ktp-sendfile.lang -f purpose_nextcloud.lang -f purpose_pastebin.lang -f purpose_phabricator.lang -f purpose_saveas.lang -f purpose_twitter.lang -f purpose_youtube.lang -f purpose_reviewboard.lang -f purpose-fileitemaction.lang
%defattr(-,root,root,-)

