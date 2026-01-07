%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 4

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _docdir %{_datadir}/doc
%define tde_datadir %{tde_prefix}/share
%endif

Name:		trinity-desktop
Version:	%{tde_version}
Release:	%{pkg_rel}
Summary:	Meta-package to install TDE
Group:		User Interface/Desktops
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

BuildArch:	noarch

#Requires:	pinentry-tqt
Requires:	trinity-tdeaccessibility >= %{version}
Requires:	trinity-tdeaddons >= %{version}
Requires:	trinity-tdeadmin >= %{version}
Requires:	trinity-tdeartwork >= %{version}
Requires:	trinity-tdebase >= %{version}
Requires:	trinity-tdebindings >= %{version}
Requires:	trinity-tdeedu >= %{version}
Requires:	trinity-tdegames >= %{version}
Requires:	trinity-tdegraphics >= %{version}
Requires:	trinity-tdemultimedia >= %{version}
Requires:	trinity-tdenetwork >= %{version}
Requires:	trinity-tdepim >= %{version}
Requires:	trinity-tdetoys >= %{version}
Requires:	trinity-tdeutils >= %{version}

%description
The TDE project aims to keep the KDE3.5 computing style alive, as well as
polish off any rough edges that were present as of KDE 3.5.10. Along
the way, new useful features will be added to keep the environment
up-to-date.
Toward that end, significant new enhancements have already been made in
areas such as display control, network connectivity, user
authentication, and much more!

%files

##########

%package devel
Group:		User Interface/Desktops
Summary:	Meta-package to install TDE development tools

Requires:	trinity-tdesdk >= %{version}
Requires:	trinity-tdevelop >= %{version}
Requires:	trinity-tdewebdev >= %{version}

%description devel
%{summary}

%files devel

##########

%package applications
Group:		User Interface/Desktops
Summary:	Meta-package to install all TDE applications

# Warning, k9copy requires ffmpeg

Requires: trinity-abakus
Requires: trinity-amarok
Requires: trinity-basket
Requires: trinity-bibletime
Requires: trinity-codeine
Requires: trinity-digikam
Requires: trinity-dolphin
Requires: trinity-filelight
Requires: trinity-gwenview
Requires: trinity-k3b
Requires: trinity-k9copy
Requires: trinity-kaffeine
Requires: trinity-kasablanca
Requires: trinity-katapult
Requires: trinity-kbarcode
Requires: trinity-kbfx
Requires: trinity-kbibtex
Requires: trinity-kbiff
Requires: trinity-kbookreader
Requires: trinity-kchmviewer
Requires: trinity-kcmautostart
# Requires: trinity-kcmldap
# Requires: trinity-kcmldapcontroller
# Requires: trinity-kcmldapmanager
Requires: trinity-kcpuload
Requires: trinity-kdbg
Requires: trinity-kdbusnotification
Requires: trinity-kdiff3
Requires: trinity-kdirstat
Requires: trinity-keep
# Requires: trinity-kerberostray
Requires: trinity-keximdb
Requires: trinity-kftpgrabber
Requires: trinity-kile
Requires: trinity-kima
Requires: trinity-kiosktool
Requires: trinity-kkbswitch
Requires: trinity-klamav
Requires: trinity-klcddimmer
Requires: trinity-kmplayer
Requires: trinity-kmyfirewall
Requires: trinity-kmymoney
Requires: trinity-knemo
Requires: trinity-knetload
Requires: trinity-knetstats
Requires: trinity-knights
Requires: trinity-knowit
Requires: trinity-knmap
Requires: trinity-knutclient
Requires: trinity-koffice-suite
Requires: trinity-kommando
Requires: trinity-kompose
Requires: trinity-konversation
Requires: trinity-kooldock
Requires: trinity-kopete-otr
Requires: trinity-kpicosim
# Requires: trinity-kpilot
Requires: trinity-kplayer
Requires: trinity-krecipes
Requires: trinity-krename
Requires: trinity-krusader
Requires: trinity-kscope
Requires: trinity-ksensors
Requires: trinity-kshowmail
Requires: trinity-kshutdown
Requires: trinity-ksplash-engine-moodin
Requires: trinity-ksquirrel
Requires: trinity-kstreamripper
Requires: trinity-ksystemlog
Requires: trinity-ktechlab
Requires: trinity-ktorrent
Requires: trinity-kvirc
Requires: trinity-kvkbd
Requires: trinity-kvpnc
Requires: trinity-kxmleditor
Requires: trinity-mathemagics
Requires: trinity-mplayerthumbs
Requires: trinity-piklab
Requires: trinity-polkit-agent-tde
Requires: trinity-potracegui
Requires: trinity-qalculate-tde
Requires: trinity-rosegarden
Requires: trinity-smb4k
# Requires: trinity-smartcardauth
Requires: trinity-soundkonverter
Requires: trinity-tastymenu
Requires: trinity-tdealternatives
Requires: trinity-tdebluez
Requires: trinity-tde-ebook-reader
# Requires: trinity-tde-guidance
Requires: trinity-tde-style-baghira
Requires: trinity-tde-style-domino
Requires: trinity-tde-style-ia-ora
Requires: trinity-tde-style-lipstik
Requires: trinity-tde-style-polyester
Requires: trinity-tde-style-qtcurve
# Requires: trinity-tde-systemsettings
Requires: trinity-tdedocker
Requires: trinity-tdeio-appinfo
# Requires: trinity-tdeio-apt
Requires: trinity-tdeio-ftps
Requires: trinity-tdeio-gopher
Requires: trinity-tdeio-locate
Requires: trinity-tdeio-sword
Requires: trinity-tdeio-umountwrapper
Requires: trinity-tdeknighttour
Requires: trinity-tdenetworkmanager
Requires: trinity-tdepacman
Requires: trinity-tdepowersave
Requires: trinity-tderadio
Requires: trinity-tdesshaskpass
Requires: trinity-tdesudo
Requires: trinity-tdesvn
Requires: trinity-tdexsldbg
Requires: trinity-tdmtheme
Requires: trinity-tellico
Requires: trinity-tork
Requires: trinity-twin-style-crystal
Requires: trinity-twin-style-dekorator
Requires: trinity-twin-style-fahrenheit
Requires: trinity-twin-style-machbunt
Requires: trinity-twin-style-mallory
Requires: trinity-twin-style-suse2
Requires: trinity-universal-indent-gui-tqt
Requires: trinity-xdg-desktop-portal-tde
# Requires: trinity-wlassistant
Requires: trinity-yakuake

# Power management
Obsoletes: trinity-tde-guidance-powermanager < %{?epoch:%{epoch}:}%{version}-%{release}

# Decoration-related stuff (not installed by default)
#Requires: trinity-kgtk-qt3
#Requires: trinity-gtk-qt-engine
#Requires: trinity-gtk3-tqt-engine
#Requires: trinity-qt4-tqt-theme-engine

# Compiz-related stuff does not work (obsolete)
#Requires: trinity-compizconfig-backend-kconfig
#Requires: trinity-desktop-effects-kde
#Requires: trinity-fusion-icon


%description applications
%{summary}

%files  applications

##########

%package all
Group:		User Interface/Desktops
Summary:	Meta-package to install all TDE packages

Requires:	%{name} = %{version}
Requires:	%{name}-applications = %{version}
Requires:	%{name}-devel = %{version}

%description all
%{summary}

%files all

%prep


%build


%install

