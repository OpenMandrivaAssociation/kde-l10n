# Supported l10n language
# to update this list (depending on which new localisations tarballs are available
# from upstream), you can use:
# $ ls SOURCES/kde-l10n*tar.bz2 | grep -v @valencia | awk -F- '{print $3}' | tr '\n' ' '
#
# Note: ca@valencia is treated differently because of the @ in the tarball name
%define langlist ar bg ca  cs da de el en_GB es et eu fi fr ga gl gu he hi hr hu ia id is it ja kk km kn ko lt lv mai nb nds nl nn pa pl pt pt_BR ro ru sk sl sr sv th tr uk wa zh_CN zh_TW

%define disabled_langs af az be bn_IN bo br bs csb cy eo fa fo fy hne ku lo mi mk ml mt mr ne se oc si ta tg ven vi xh

%define build_ca_valencia 1

%{expand:%(for lang in %disabled_langs; do echo "%%{expand:%%define build_$lang 0"}; done)}

%{expand:%(for lang in %langlist; do echo "%%{expand:%%define build_$lang 1"}; done)}

Name: kde-l10n
Version: 4.6.4
Release: 1
Epoch: 3
Url: http://www.kde.org
Summary: Internationalization support for KDE
Group: System/Internationalization
License: LGPLv2
BuildArch: noarch
# l10n sources
# list ca@valencia tarball separately due to the @ in the tarball name
Source1: kde-l10n-ca@valencia-%{version}.tar.bz2
%{expand:%(\
	i=2; \
	for lang in %langlist; do\
		echo "%%{expand:Source$i: %%{_sourcedir}/%%{name}-$lang-%%{version}.tar.bz2}";\
		i=$[i+1];\
	done\
	)
}
# copy from kde-l10n-4.4.5, it only contains kdepim translations
Source500: kde-l10n-kdepim-4.4.5.tar.bz2
BuildRequires: findutils
BuildRequires: gettext
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtd42-xml
BuildRequires: cmake
BuildRequires: kdelibs4-devel >= %{version}

%description
Internationalization support for KDE.

#--------------------------------------------------------------------

%package en_US
Summary: American English support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-en
Provides: %{name}-American
Conflicts: konq-plugins < 1:4.6.1
%description en_US
%{summary}.

This is an empty package, en_US support is already provided by kdelibs4.

%files en_US

#--------------------------------------------------------------------
%if %{build_af}
%package af
Summary: Afrikaans language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Afrikaans = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description af
%{summary}.

%files af

%{_datadir}/locale/af/LC_MESSAGES/*
%{_datadir}/locale/af/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_ar}
%package ar
Summary: Arabic language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ar
Provides: %{name}-Arabic = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1

%description ar
%{summary}.

%files ar

%{_datadir}/locale/ar/LC_MESSAGES/*
%{_datadir}/locale/ar/entry.desktop
%{_datadir}/locale/ar/LC_SCRIPTS/
%{_kde_appsdir}/klettres/ar/
%endif
#--------------------------------------------------------------------
%if %{build_az}
%package az
Summary: Azerbaijani language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Azerbaijani = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1

%description az
%{summary}.

%files az

%{_datadir}/locale/az/LC_MESSAGES/*
%{_datadir}/locale/az/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_eu}
%package eu
Summary: Basque language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-eu
Provides: %{name}-Basque = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1

%description eu
%{summary}.

%files eu

%{_datadir}/locale/eu/LC_MESSAGES/*
%{_datadir}/locale/eu/entry.desktop
%{_kde_docdir}/HTML/eu/*
%endif
#--------------------------------------------------------------------
%if %{build_be}
%package be
Summary: Belarusian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Belarusian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1

%description be
%{summary}.

%files be

%{_datadir}/locale/be/LC_MESSAGES/*
%{_datadir}/locale/be/entry.desktop
%endif
#--------------------------------------------------------------------
%if %{build_bn_IN}
%package bn_IN
Summary: Bengali India language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-bn
Provides: %{name}-Bengali-India = %{version}-%{release}
Provides: %{name}-Bengali = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1

%description bn_IN
%{summary}.

%files bn_IN

%{_datadir}/locale/bn_IN/LC_MESSAGES/*
%{_datadir}/locale/bn_IN/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_bg}
%package bg
Summary: Bulgarian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-bg
Provides: %{name}-Bulgarian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description bg
%{summary}.

%files bg

%{_datadir}/locale/bg/LC_MESSAGES/*
%{_datadir}/locale/bg/entry.desktop
%{_kde_appsdir}/kvtml/bg/
%endif
#--------------------------------------------------------------------

%if %{build_bo}
%package bo
Summary: Tibetan language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Tibetan = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description bo
%{summary}.

%files bo

%{_datadir}/locale/bo/LC_MESSAGES/*
%{_datadir}/locale/bo/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_br}
%package br
Summary: Breton language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Breton = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description br
%{summary}.

%files br

%{_datadir}/locale/br/LC_MESSAGES/*
%{_datadir}/locale/br/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_bs}
%package bs
Summary: Bosnian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Bosnian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description bs
%{summary}.

%files bs

%{_datadir}/locale/bs/LC_MESSAGES/*
%{_datadir}/locale/bs/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_ca}
%package ca
Summary: Catalan language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ca
Provides: %{name}-Catalan = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ca
%{summary}.

%files ca

%{_datadir}/locale/ca/LC_MESSAGES/*
%{_datadir}/locale/ca/LC_SCRIPTS/
%{_datadir}/locale/ca/entry.desktop
%{_kde_appsdir}/khangman/ca.txt
%{_kde_appsdir}/ktuberling/sounds/ca*
%{_kde_appsdir}/kvtml/ca/
%{_kde_docdir}/HTML/ca/*
%{_kde_mandir}/ca/*/*
%endif
#--------------------------------------------------------------------

%if %{build_ca_valencia}
%package ca-valencia
Summary: Catalan (Valencian) language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Catalan-Valencian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ca-valencia
%{summary}.

%files ca-valencia

%{_datadir}/locale/ca@valencia/LC_MESSAGES/*
%{_datadir}/locale/ca@valencia/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_cs}
%package cs
Summary: Czech language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-cs
Provides: %{name}-Czech = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description cs
%{summary}.

%files cs

%{_datadir}/locale/cs/LC_MESSAGES/*
%{_datadir}/locale/cs/entry.desktop
%{_kde_appsdir}/khangman/cs.txt
%{_kde_appsdir}/klettres/cs/
%{_kde_appsdir}/kvtml/cs/
%{_kde_docdir}/HTML/cs/*
%endif
#--------------------------------------------------------------------

%if %{build_csb}
%package csb
Summary: Kashubian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-pl
Provides: %{name}-Kashubian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description csb
%{summary}.

%files csb

%{_datadir}/locale/csb/LC_MESSAGES/*
%{_datadir}/locale/csb/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_cy}
%package cy
Summary: Welsh language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Welsh = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description cy
%{summary}.

%files cy

%{_datadir}/locale/cy/LC_MESSAGES/*
%{_datadir}/locale/cy/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_da}
%package da
Summary: Danish language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-da
Provides: %{name}-Danish = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description da
%{summary}.

%files da

%{_datadir}/locale/da/LC_MESSAGES/*
%{_datadir}/locale/da/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/da*
%{_kde_appsdir}/khangman/da.txt
%{_kde_appsdir}/klettres/da/
%{_kde_appsdir}/kvtml/da/
%{_kde_docdir}/HTML/da/*
%{_kde_mandir}/da/*/*
%endif
#--------------------------------------------------------------------

%if %{build_de}
%package de
Summary: German language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-de
Provides: %{name}-German = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description de
%{summary}.

%files de

%{_datadir}/locale/de/LC_MESSAGES/*
%{_datadir}/locale/de/LC_SCRIPTS/
%{_datadir}/locale/de/entry.desktop
%{_kde_appsdir}/klettres/de/
%{_kde_appsdir}/ktuberling/sounds/de*
%{_kde_appsdir}/khangman/de.txt
%{_kde_appsdir}/kvtml/de/
%{_kde_appsdir}/step/objinfo/l10n/de/
%{_kde_docdir}/HTML/de/*
%{_kde_mandir}/de/*/*
%endif
#--------------------------------------------------------------------

%if %{build_el}
%package el
Summary: Greek language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-el
Provides: %{name}-Greek = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description el
%{summary}.

%files el

%{_datadir}/locale/el/LC_MESSAGES/*
%{_datadir}/locale/el/entry.desktop
%{_kde_appsdir}/kvtml/el
%{_kde_docdir}/HTML/el/
%{_kde_appsdir}/ktuberling/sounds/el*
%{_kde_mandir}/el/*/*
%endif
#--------------------------------------------------------------------

%if %{build_gu}
%package gu
Summary: Gujarati language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-gu
Provides: %{name}-Gujarati = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description gu
%{summary}.

%files gu

%{_datadir}/locale/gu/LC_MESSAGES/*
%{_datadir}/locale/gu/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_en_GB}
%package en_GB
Summary: British English support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-en
Provides: %{name}-British
Conflicts: konq-plugins < 1:4.6.1
%description en_GB
%{summary}.

%files en_GB

%{_datadir}/locale/en_GB/LC_MESSAGES/*
%{_datadir}/locale/en_GB/entry.desktop
%{_kde_appsdir}/klettres/en_GB/
%{_kde_appsdir}/kvtml/en_GB/
%{_kde_docdir}/HTML/en_GB/
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.en_GB.xml
%{_kde_appsdir}/kturtle/data/logokeywords.en_GB.xml
%{_kde_appsdir}/kturtle/examples/en_GB/
%endif
#--------------------------------------------------------------------

%if %{build_eo}
%package eo
Summary: Esperanto support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-eo
Provides: %{name}-Esperanto = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description eo
%{summary}.

%files eo

%{_datadir}/locale/eo/LC_MESSAGES/*
%{_datadir}/locale/eo/entry.desktop
%{_kde_docdir}/HTML/eo/*
%endif
#--------------------------------------------------------------------

%if %{build_es}
%package es
Summary: Spanish language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-es
Provides: %{name}-Spanish = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description es
%{summary}.

%files es

%{_datadir}/locale/es/LC_MESSAGES/*
%{_datadir}/locale/es/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/es*
%{_kde_appsdir}/khangman/es.txt
%{_kde_appsdir}/klettres/es/
%{_kde_appsdir}/kvtml/es/
%{_kde_docdir}/HTML/es/*
%{_kde_mandir}/es/*/*
%endif
#--------------------------------------------------------------------

%if %{build_et}
%package et
Summary: Estonian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-et
Provides: %{name}-Estonian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description et
%{summary}.

%files et

%{_datadir}/locale/et/LC_MESSAGES/*
%{_datadir}/locale/et/entry.desktop
%{_kde_appsdir}/khangman/et.txt
%{_kde_appsdir}/kvtml/et/
%{_kde_docdir}/HTML/et/*
%{_kde_mandir}/et/*/*
%endif
#--------------------------------------------------------------------

%if %{build_fa}
%package fa
Summary: Farsi language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-fa
Provides: %{name}-Farsi = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description fa
%{summary}.

%files fa

%{_datadir}/locale/fa/LC_MESSAGES/*
%{_datadir}/locale/fa/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_fi}
%package fi
Summary: Finnish language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-fi
Provides: %{name}-Finnish = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description fi
%{summary}.

%files fi

%{_datadir}/locale/fi/LC_MESSAGES/*
%{_datadir}/locale/fi/entry.desktop
%{_datadir}/locale/fi/LC_SCRIPTS/
%{_kde_appsdir}/khangman/fi.txt
%{_kde_appsdir}/ktuberling/sounds/fi*
%{_kde_appsdir}/kvtml/fi/
%endif
#--------------------------------------------------------------------

%if %{build_fo}
%package fo
Summary: Faroese language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Faroese = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description fo
%{summary}.

%files fo

%{_datadir}/locale/fo/LC_MESSAGES/*
%{_datadir}/locale/fo/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_fr}
%package fr
Summary: French language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-fr
Provides: %{name}-French = %{version}-%{release}
Conflicts: nepomuk-scribo < 1:0.6.1-1
Conflicts: konq-plugins < 1:4.6.1
%description fr
%{summary}.

%files fr

%{_datadir}/locale/fr/LC_MESSAGES/*
%{_datadir}/locale/fr/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/fr*
%{_kde_appsdir}/khangman/fr.txt
%{_kde_appsdir}/kvtml/fr/
%{_kde_docdir}/HTML/fr/*
%{_kde_mandir}/fr/*/*
%endif
#--------------------------------------------------------------------

%if %{build_fy}
%package fy
Summary: Frisian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-fy
Provides: %{name}-Frisian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description fy
%{summary}.

%files fy

%{_datadir}/locale/fy/LC_MESSAGES/*
%{_datadir}/locale/fy/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_ga}
%package ga
Summary: Irish language support for KDE
Group: System/Internationalization
Obsoletes: kde-i18n-Gaeilge
Provides: %{name} = %{version}
Requires: locales-ga
Provides: %{name}-Irish = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ga
%{summary}.

%files ga

%{_datadir}/locale/ga/LC_MESSAGES/*
%{_datadir}/locale/ga/LC_SCRIPTS/
%{_datadir}/locale/ga/entry.desktop
%{_kde_appsdir}/khangman/ga.txt
%{_kde_appsdir}/ktuberling/sounds/ga*
%{_kde_appsdir}/kvtml/ga/
%endif
#--------------------------------------------------------------------

%if %{build_gl}
%package gl
Summary: Galician language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-gl
Provides: %{name}-Galician = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description gl
%{summary}.

%files gl

%{_datadir}/locale/gl/LC_MESSAGES/*
%{_datadir}/locale/gl/entry.desktop
%{_kde_appsdir}/kvtml/gl/
%{_kde_appsdir}/ktuberling/sounds/gl.soundtheme
%{_kde_appsdir}/ktuberling/sounds/gl/
%{_kde_docdir}/HTML/gl/*
%{_kde_mandir}/gl/*/*
%endif
#--------------------------------------------------------------------

%if %{build_he}
%package he
Summary: Hebrew language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-he
Provides: %{name}-Hebrew = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description he
%{summary}.

%files he

%{_datadir}/locale/he/LC_MESSAGES/*
%{_datadir}/locale/he/entry.desktop
%{_kde_appsdir}/klettres/he/
%{_kde_docdir}/HTML/he/*
%endif
#--------------------------------------------------------------------

%if %{build_hi}
%package hi
Summary: Hindi language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-hi
Provides: %{name}-Hindi = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description hi
%{summary}.

%files hi

%{_datadir}/locale/hi/LC_MESSAGES/*
%{_datadir}/locale/hi/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_hne}
%package hne
Summary: Chhattisgarhi language support for KDE 
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-hne
Provides: %{name}-Chhattisgarhi = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description hne
%{summary}.

%files hne
%defattr(-,root,root,-)
%{_datadir}/locale/hne/LC_MESSAGES/*
%{_datadir}/locale/hne/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_hr}
%package hr
Summary: Croatian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-hr
Provides: %{name}-Croatian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description hr
%{summary}.

%files hr

%{_datadir}/locale/hr/LC_MESSAGES/*
%{_datadir}/locale/hr/entry.desktop
%{_datadir}/locale/hr/LC_SCRIPTS
%endif
#--------------------------------------------------------------------

%if %{build_hu}
%package hu
Summary: Hungarian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-hu
Provides: %{name}-Hungarian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description hu
%{summary}.

%files hu

%{_datadir}/locale/hu/LC_MESSAGES/*
%{_datadir}/locale/hu/entry.desktop
%{_kde_appsdir}/khangman/hu.txt
%{_kde_appsdir}/kvtml/hu/
%{_kde_appsdir}/klettres/hu/
%{_kde_docdir}/HTML/hu/*
%endif
#--------------------------------------------------------------------

%if %{build_ia}
%package ia
Summary: Interlingua language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Interlingua = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ia
%{summary}.

%files ia
%{_datadir}/locale/ia/LC_MESSAGES/*
%{_datadir}/locale/ia/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_id}
%package id
Summary: Indonesian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-id
Provides: %{name}-Indonesian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description id
%{summary}.

%files id

%{_datadir}/locale/id/LC_MESSAGES/*
%{_datadir}/locale/id/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_is}
%package is
Summary: Icelandic language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-is
Provides: %{name}-Icelandic = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description is
%{summary}.

%files is

%{_datadir}/locale/is/LC_MESSAGES/*
%{_datadir}/locale/is/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_it}
%package it
Summary: Italian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-it
Provides: %{name}-Italian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description it
%{summary}.

%files it

%{_datadir}/locale/it/LC_MESSAGES/*
%{_datadir}/locale/it/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/it*
%{_kde_appsdir}/klettres/it/
%{_kde_appsdir}/kvtml/it/
%{_kde_docdir}/HTML/it/*
%{_kde_appsdir}/step/objinfo/l10n/it/
%{_kde_mandir}/it/*/*
%endif
#--------------------------------------------------------------------

%if %{build_ja}
%package ja
Summary: Japanese language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ja
Provides: %{name}-Japanese = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ja
%{summary}.

%files ja

%{_datadir}/locale/ja/LC_MESSAGES/*
%{_datadir}/locale/ja/LC_SCRIPTS/
%{_datadir}/locale/ja/entry.desktop
%{_kde_docdir}/HTML/ja/*
%endif
#--------------------------------------------------------------------

%if %{build_kn}
%package kn
Summary: Kannada language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-kn
Provides: %{name}-Kannada = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description kn
%{summary}.

%files kn

%{_datadir}/locale/kn/LC_MESSAGES/*
%{_datadir}/locale/kn/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_kk}
%package kk
Summary: Kazakh language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-kk
Provides: %{name}-Kazakh = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description kk
%{summary}.

%files kk

%{_datadir}/locale/kk/LC_MESSAGES/*
%{_datadir}/locale/kk/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_km}
%package km
Summary: Khmer language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-km
Provides: %{name}-Khmer = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description km
%{summary}.

%files km

%{_datadir}/locale/km/LC_MESSAGES/*
%{_datadir}/locale/km/entry.desktop
%{_datadir}/locale/km/flag.png
%endif
#--------------------------------------------------------------------

%if %{build_ko}
%package ko
Summary: Korean language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ko
Provides: %{name}-Korean = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ko
%{summary}.

%files ko

%{_datadir}/locale/ko/LC_MESSAGES/*
%{_datadir}/locale/ko/LC_SCRIPTS/
%{_datadir}/locale/ko/entry.desktop
%{_kde_docdir}/HTML/ko/*
%endif
#--------------------------------------------------------------------

%if %{build_ku}
%package ku
Summary: Kurdish language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ku
Provides: %{name}-Kurdish = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ku
%{summary}.


%files ku

%{_datadir}/locale/ku/LC_MESSAGES/*
%{_datadir}/locale/ku/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_lo}
%package lo
Summary: Lao language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Lao = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description lo
%{summary}.

%files lo

%{_datadir}/locale/lo/LC_MESSAGES/*
%{_datadir}/locale/lo/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_lt}
%package lt
Summary: Lithuanian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-lt
Provides: %{name}-Lithuanian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description lt
%{summary}.

%files lt

%{_datadir}/locale/lt/LC_MESSAGES/*
%{_datadir}/locale/lt/LC_SCRIPTS/
%{_datadir}/locale/lt/entry.desktop
%{_kde_docdir}/HTML/lt/*
%{_kde_mandir}/lt/*/*
%endif
#--------------------------------------------------------------------

%if %{build_lv}
%package lv
Summary: Latvian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-lv
Provides: %{name}-Latvian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description lv
%{summary}.

%files lv

%{_datadir}/locale/lv/LC_MESSAGES/*
%{_datadir}/locale/lv/entry.desktop
%{_datadir}/locale/lv/LC_SCRIPTS
%endif
#--------------------------------------------------------------------

%if %{build_nds}
%package nds
Summary: Low Saxon language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-nds
Provides: %{name}-LowSaxon = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description nds
%{summary}.

%files nds

%{_datadir}/locale/nds/LC_MESSAGES/*
%{_datadir}/locale/nds/entry.desktop
%{_kde_appsdir}/klettres/nds/
%{_kde_appsdir}/khangman/nds.txt
%{_kde_appsdir}/kvtml/nds/
%{_kde_appsdir}/ktuberling/sounds/nds*
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.nds.xml
%{_kde_appsdir}/kturtle/examples/nds
%{_kde_docdir}/HTML/nds/*
%endif
#--------------------------------------------------------------------

%if %{build_mi}
%package mi
Summary: Maori language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Maori = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description mi
%{summary}.

%files mi

%{_datadir}/locale/mi/LC_MESSAGES/*
%{_datadir}/locale/mi/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_mk}
%package mk
Summary: Macedonian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-mk
Provides: %{name}-Macedonian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description mk
%{summary}.

%files mk

%{_datadir}/locale/mk/LC_MESSAGES/*
%{_datadir}/locale/mk/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_mai}
%package mai
Summary: Maithili language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-mai
Provides: %{name}-Maithili = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description mai
%{summary}.

%files mai

%{_datadir}/locale/mai/LC_MESSAGES/*
%{_datadir}/locale/mai/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_ml}
%package ml
Summary: Malayalam language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ml
Provides: %{name}-Malayalam = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ml
%{summary}.

%files ml

%{_datadir}/locale/ml/LC_MESSAGES/*
%{_datadir}/locale/ml/LC_SCRIPTS/
%{_datadir}/locale/ml/entry.desktop
%{_kde_appsdir}/klettres/ml/
%endif
#--------------------------------------------------------------------

%if %{build_mt}
%package mt
Summary: Maltese language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Maltese = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description mt
%{summary}.

%files mt

%{_datadir}/locale/mt/LC_MESSAGES/*
%{_datadir}/locale/mt/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_mr}
%package mr
Summary: Marathi language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ca
Provides: %{name}-Marathi = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description mr
%{summary}.

%files mr

%{_datadir}/locale/mr/LC_MESSAGES/*
%{_datadir}/locale/mr/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_ne}
%package ne
Summary: Nepali language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ne
Provides: %{name}-Nepali = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ne
%{summary}.

%files ne

%{_datadir}/locale/ne/LC_MESSAGES/*
%{_datadir}/locale/ne/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_nl}
%package nl
Summary: Dutch language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-nl
Provides: %{name}-nl = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description nl
%{summary}.

%files nl

%{_datadir}/locale/nl/LC_MESSAGES/*
%{_datadir}/locale/nl/LC_SCRIPTS/
%{_datadir}/locale/nl/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/nl*
%{_kde_appsdir}/klettres/nl/
%{_kde_appsdir}/kvtml/nl/
%{_kde_docdir}/HTML/nl/*
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.nl.xml
%{_kde_appsdir}/kturtle/data/logokeywords.nl.xml
%{_kde_appsdir}/kturtle/examples/nl/*.logo
%{_kde_mandir}/nl/*/*
%endif
#--------------------------------------------------------------------

%if %{build_se}
%package se
Summary: Northern Sami language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-se
Provides: %{name}-NorthernSami = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description se
%{summary}.

%files se

%{_datadir}/locale/se/LC_MESSAGES/*
%{_datadir}/locale/se/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_nb}
%package nb
Summary: Norwegian (Bokmaal) language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-nb
Provides: %{name}-Norwegian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description nb
%{summary}.

%files nb

%{_datadir}/locale/nb/LC_MESSAGES/*
%{_datadir}/locale/nb/LC_SCRIPTS/
%{_datadir}/locale/nb/entry.desktop
%{_kde_appsdir}/khangman/nb.txt
%{_kde_appsdir}/kvtml/nb/
%{_kde_docdir}/HTML/nb/*
%{_kde_appsdir}/klettres/nb/
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.nb.xml
%{_kde_appsdir}/kturtle/data/logokeywords.nb.xml
%{_kde_appsdir}/kturtle/examples/nb/*.logo
%{_kde_mandir}/nb/*/*
%endif
#--------------------------------------------------------------------

%if %{build_nn}
%package nn
Summary: Norwegian (Nynorsk) language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-nn
Provides: %{name}-Norwegian-Nynorsk = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description nn
%{summary}.

%files nn

%{_datadir}/locale/nn/LC_MESSAGES/*
%{_datadir}/locale/nn/LC_SCRIPTS/
%{_datadir}/locale/nn/entry.desktop
%{_kde_appsdir}/khangman/nn.txt
%{_kde_appsdir}/kvtml/nn/
%{_kde_docdir}/HTML/nn/*
%endif
#--------------------------------------------------------------------

%if %{build_oc}
%package oc
Summary: Occitan language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Occitan = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description oc
%{summary}.

%files oc

%{_datadir}/locale/oc/LC_MESSAGES/*
%{_datadir}/locale/oc/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_pl}
%package pl
Summary: Polish language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-pl
Provides: %{name}-Polish= %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description pl
%{summary}.

%files pl

%{_datadir}/locale/pl/LC_MESSAGES/*
%{_datadir}/locale/pl/LC_SCRIPTS/
%{_datadir}/locale/pl/entry.desktop
%{_kde_appsdir}/khangman/pl.txt
%{_kde_appsdir}/kvtml/pl/
%{_kde_docdir}/HTML/pl/*
%{_kde_mandir}/pl/*/*
%endif
#--------------------------------------------------------------------

%if %{build_pt}
%package pt
Summary: Portuguese language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-pt
Provides: %{name}-Portuguese = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description pt
%{summary}.

%files pt

%{_datadir}/locale/pt/LC_MESSAGES/*
%{_datadir}/locale/pt/entry.desktop
%{_kde_appsdir}/khangman/pt.txt
%{_kde_appsdir}/ktuberling/sounds/pt*
%{_kde_appsdir}/kvtml/pt/
%{_kde_docdir}/HTML/pt/*
%{_kde_mandir}/pt/*/*
%endif
#--------------------------------------------------------------------

%if %{build_pa}
%package pa
Summary: Punjabi language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-pa
Provides: %{name}-Punjabi = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description pa
%{summary}.

%files pa

%{_datadir}/locale/pa/LC_MESSAGES/*
%{_datadir}/locale/pa/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_pt_BR}
%package pt_BR
Summary: Brazil Portuguese language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-pt
Provides: %{name}-Brazil = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description pt_BR
%{summary}.

%files pt_BR

%{_datadir}/locale/pt_BR/LC_MESSAGES/*
%{_datadir}/locale/pt_BR/entry.desktop
%{_kde_appsdir}/khangman/pt_BR.txt
%{_kde_appsdir}/klettres/pt_BR/*
%{_kde_appsdir}/kvtml/pt_BR/
%{_kde_docdir}/HTML/pt_BR/*
%{_kde_mandir}/pt_BR/*/*
%endif
#--------------------------------------------------------------------

%if %{build_ro}
%package ro
Summary: Romanian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ro
Provides: %{name}-Romanian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ro
%{summary}.

%files ro

%{_datadir}/locale/ro/LC_MESSAGES/*
%{_datadir}/locale/ro/entry.desktop
%{_kde_appsdir}/kvtml/ro/
%{_kde_appsdir}/ktuberling/sounds/ro*
%{_kde_docdir}/HTML/ro/*
%endif
#--------------------------------------------------------------------

%if %{build_ru}
%package ru
Summary: Russian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ru
Provides: %{name}-Russian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ru
%{summary}.

%files ru

%{_datadir}/locale/ru/LC_MESSAGES/*
%{_datadir}/locale/ru/LC_SCRIPTS/
%{_datadir}/locale/ru/entry.desktop
%{_kde_appsdir}/kvtml/ru/
%{_kde_docdir}/HTML/ru/*
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.ru.xml
%{_kde_appsdir}/kturtle/data/logokeywords.ru.xml
%{_kde_appsdir}/kturtle/examples/ru/*.logo
%{_kde_appsdir}/klettres/ru
%{_kde_appsdir}/ktuberling/sounds/ru/
%{_kde_appsdir}/ktuberling/sounds/ru.soundtheme
%{_kde_mandir}/ru/*/*
%endif
#--------------------------------------------------------------------

%if %{build_si}
%package si
Summary: Sinhala language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-si
Provides: %{name}-Sinhala = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description si
%{summary}.

%files si

%{_datadir}/locale/si/LC_MESSAGES/*
%{_datadir}/locale/si/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_sk}
%package sk
Summary: Slovak language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-sk
Provides: %{name}-Slovak = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description sk
%{summary}.

%files sk

%{_datadir}/locale/sk/LC_MESSAGES/*
%{_datadir}/locale/sk/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_sl}
%package sl
Summary: Slovenian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-sl
Provides: %{name}-Slovenian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description sl
%{summary}.

%files sl

%{_datadir}/locale/sl/LC_MESSAGES/*
%{_datadir}/locale/sl/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/sl*
%{_kde_appsdir}/khangman/sl.txt
%{_kde_appsdir}/kvtml/sl/
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.sl.xml
%{_kde_appsdir}/kturtle/data/logokeywords.sl.xml
%{_kde_appsdir}/kturtle/examples/sl/*.logo
%{_kde_docdir}/HTML/sl/*
%endif
#--------------------------------------------------------------------

%if %{build_sr}
%package sr
Summary: Serbian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-sr
Provides: %{name}-Serbian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description sr
%{summary}.

%files sr

%{_datadir}/locale/sr/LC_MESSAGES/*
%{_datadir}/locale/sr/LC_SCRIPTS/
%{_datadir}/locale/sr/entry.desktop
%{_datadir}/locale/sr@latin/entry.desktop
%{_datadir}/locale/sr@latin/LC_MESSAGES/*
%{_datadir}/locale/sr@latin/LC_SCRIPTS/
%{_datadir}/locale/sr@ijekavianlatin/entry.desktop
%{_datadir}/locale/sr@ijekavianlatin/LC_MESSAGES/*
%{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/
%{_datadir}/locale/sr@ijekavian/LC_MESSAGES/*
%{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/
%{_datadir}/locale/sr@ijekavian/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/sr*
%{_kde_docdir}/HTML/sr/*
%{_kde_docdir}/HTML/sr@latin/*
%{_kde_iconsdir}/*/*/*/*/sr/
%{_kde_iconsdir}/*/*/*/*/sr@latin/
%{_kde_iconsdir}/*/*/*/*/sr@ijekavian/
%{_kde_iconsdir}/*/*/*/*/sr@ijekavianlatin/
%{_kde_appsdir}/desktoptheme/*/widgets/l10n/sr
%{_kde_appsdir}/desktoptheme/*/widgets/l10n/sr@latin
%{_kde_appsdir}/desktoptheme/*/widgets/l10n/sr@ijekavian
%{_kde_appsdir}/desktoptheme/*/widgets/l10n/sr@ijekavianlatin
%{_kde_appsdir}/desktoptheme/default/icons/l10n/sr*
%{_kde_appsdir}/khangman/sr@latin.txt
%{_kde_appsdir}/kvtml/sr*/
%{_kde_mandir}/sr/*/*
%{_kde_mandir}/sr@latin/*/*
%endif
#--------------------------------------------------------------------

%if %{build_sv}
%package sv
Summary: Swedish language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-sv
Provides: %{name}-Swedish = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description sv
%{summary}.

%files sv

%{_datadir}/locale/sv/LC_MESSAGES/*
%{_datadir}/locale/sv/entry.desktop
%{_datadir}/locale/sv/LC_SCRIPTS/
%{_kde_appsdir}/ktuberling/sounds/sv*
%{_kde_appsdir}/khangman/sv.txt
%{_kde_appsdir}/kvtml/sv/
%{_kde_docdir}/HTML/sv/*
%{_kde_mandir}/sv/*/*
%endif
#--------------------------------------------------------------------
%if %{build_ta}
%package ta
Summary: Tamil language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-ta
Provides: %{name}-Tamil = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ta
%{summary}.

%files ta

%{_datadir}/locale/ta/LC_MESSAGES/*
%{_datadir}/locale/ta/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_tg}
%package tg
Summary: Tajik language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-tg
Provides: %{name}-Tajik = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description tg
%{summary}.

%files tg

%{_datadir}/locale/tg/LC_MESSAGES/*
%{_datadir}/locale/tg/entry.desktop
%{_kde_appsdir}/kvtml/tg/
%{_kde_appsdir}/khangman/tg.txt
%endif
#--------------------------------------------------------------------

%if %{build_th}
%package th
Summary: Thai language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-th
Provides: %{name}-Thai = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description th
%{summary}.

%files th

%{_datadir}/locale/th/LC_MESSAGES/*
%{_datadir}/locale/th/charset
%{_datadir}/locale/th/entry.desktop
%{_datadir}/locale/th/flag.png
%endif
#--------------------------------------------------------------------

%if %{build_tr}
%package tr
Summary: Turkish language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-tr
Provides: %{name}-Turkish = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description tr
%{summary}.

%files tr

%{_datadir}/locale/tr/LC_MESSAGES/*
%{_datadir}/locale/tr/entry.desktop
%{_kde_appsdir}/khangman/tr.txt
%{_kde_appsdir}/kvtml/tr/
%{_kde_docdir}/HTML/tr/*
%endif
#--------------------------------------------------------------------

%if %{build_uk}
%package uk
Summary: Ukrainian language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-uk
Provides: %{name}-Ukrainian = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description uk
%{summary}.

%files uk

%{_datadir}/locale/uk/LC_MESSAGES/*
%{_datadir}/locale/uk/LC_SCRIPTS/
%{_datadir}/locale/uk/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/uk*
%{_kde_appsdir}/step/objinfo/l10n/uk/
%{_kde_appsdir}/kvtml/uk/
%{_kde_appsdir}/klettres/uk/
%{_kde_docdir}/HTML/uk/*
%{_kde_mandir}/uk/*/*
%endif
#--------------------------------------------------------------------

%if %{build_ven}
%package ven
Summary: Venda language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Venda = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description ven
%{summary}.

%files ven

%{_datadir}/locale/ven/LC_MESSAGES/*
%{_datadir}/locale/ven/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_vi}
%package vi
Summary: Vietnamese language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Vietnamese= %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description vi
%{summary}.

%files vi

%{_datadir}/locale/vi/LC_MESSAGES/*
%{_datadir}/locale/vi/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_wa}
%package wa
Summary: Walloon language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-wa
Provides: %{name}-Walloon = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description wa
%{summary}.


%files wa
%{_datadir}/locale/wa/LC_MESSAGES/*
%{_datadir}/locale/wa/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/wa*
%{_kde_docdir}/HTML/wa/*
%endif
#--------------------------------------------------------------------

%if %{build_xh}
%package xh
Summary: Xhosa (a Bantu language) support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Provides: %{name}-Xhosa = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description xh
%{summary}.

%files xh
%{_datadir}/locale/xh/LC_MESSAGES/*
%{_datadir}/locale/xh/entry.desktop
%endif
#--------------------------------------------------------------------

%if %{build_zh_CN}
%package zh_CN
Summary: Chinese (Simplified Chinese) language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-zh
Provides: %{name}-Chinese = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description zh_CN
%{summary}.

%files zh_CN
%{_datadir}/locale/zh_CN/LC_MESSAGES/*
%{_datadir}/locale/zh_CN/LC_SCRIPTS/
%{_datadir}/locale/zh_CN/charset
%{_datadir}/locale/zh_CN/entry.desktop
%{_datadir}/locale/zh_CN/flag.png
%{_kde_appsdir}/kvtml/zh_CN/
%{_kde_appsdir}/step/objinfo/l10n/zh_CN/
%{_kde_docdir}/HTML/zh_CN/*
%endif
#--------------------------------------------------------------------

%if %{build_zh_TW}
%package zh_TW
Summary: Chinese (Traditional) language support for KDE
Group: System/Internationalization
Provides: %{name} = %{version}
Requires: locales-zh
Provides: %{name}-Chinese-Traditional = %{version}-%{release}
Conflicts: konq-plugins < 1:4.6.1
%description zh_TW
%{summary}.

%files zh_TW
%{_datadir}/locale/zh_TW/LC_MESSAGES/*
%{_datadir}/locale/zh_TW/entry.desktop
%{_kde_docdir}/HTML/zh_TW/*
%endif
#--------------------------------------------------------------------


%prep
%setup -T -q -n %{name}-%{version} -c

for lang in %langlist ; do
  echo $lang | grep -v '^#' && \
  bzip2 -dc %{_sourcedir}/%{name}-$lang-%{version}.tar.bz2 | tar -xf -
done

%if %{build_ca_valencia}
tar -xf %{_sourcedir}/%{name}-ca@valencia-%{version}.tar.bz2
%endif

# upstream patches
bzip2 -dc %{SOURCE500} | tar -xf -

%build
for lang in %langlist ; do
if [ -d "%_builddir/%{name}-%{version}/%{name}-$lang-%{version}" -a -d "%_builddir/%{name}-%{version}/kde-l10n-4.4.5/kde-l10n-$lang-4.4.5" ]; then
    cp -a %_builddir/%{name}-%{version}/kde-l10n-4.4.5/kde-l10n-$lang-4.4.5/* %_builddir/%{name}-%{version}/%{name}-$lang-%{version}/
    rm -rfv %_builddir/%{name}-%{version}/kde-l10n-4.4.5/kde-l10n-$lang-4.4.5
fi
#  if [ -d "%_builddir/%{name}-%{version}/%{name}-$i-%{version}" ]; then
#  pushd %_builddir/%{name}-%{version}/%{name}-$i-%{version}
#  for j in . sr@latin ; do
#    if [ -d $j ] ; then
#      # remove bogus duplicated kdepim stuff from kdenetwork
#      if [ -e $j/docs/kdenetwork/CMakeLists.txt ] ; then
#        sed -i -e 's/add_subdirectory( *korn *)/#add_subdirectory(korn)/g' -e 's/add_subdirectory( *kmail *)/#add_subdirectory(kmail)/g' -e 's/add_subdirectory( *knode *)/#add_subdirectory(knode)/g' $j/docs/kdenetwork/CMakeLists.txt
#      fi
#      # some languages still ship the kpilot stuff
#      # zap it so the kpilot package can ship all translations itself
#      rm -f $j/messages/kdepim/kpilot.po
#      if [ -e $j/docs/kdepim/CMakeLists.txt ] ; then
#        sed -i -e 's/add_subdirectory( *kpilot *)/#add_subdirectory(kpilot)/g' $j/docs/kdepim/CMakeLists.txt
#      fi
#    fi
#    done
pushd %_builddir/%{name}-%{version}/%{name}-$lang-%{version}
      %{cmake_kde4}
      %make
popd

done

# build ca@valencia separately due to the @ in the tarball name
%if %{build_ca_valencia}
pushd %_builddir/%{name}-%{version}/%{name}-ca@valencia-%{version}
      %{cmake_kde4}
      %make
popd
%endif

%install
for lang in %langlist ; do
pushd %_builddir/%{name}-%{version}/%{name}-$lang-%{version}
     %makeinstall_std -C build
done

# install ca@valencia separately due to the @ in the tarball name
%if %{build_ca_valencia}
pushd %_builddir/%{name}-%{version}/%{name}-ca@valencia-%{version}
     %makeinstall_std -C build
popd
%endif

