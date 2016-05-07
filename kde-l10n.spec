# Supported l10n language
# to update this list (depending on which new localisations tarballs are available
# from upstream), you can use:
# $ ls SOURCES/kde-l10n*tar.bz2 | grep -v @valencia | awk -F- '{print $3}' | tr '\n' ' '
#
# Note: ca@valencia is treated differently because of the @ in the tarball name
%define langlist ar bg bs ca cs da de el en_GB eo es et eu fa fi fr ga gl he hi hr hu ia id is it ja kk km ko lt lv mr nb nds nl nn pa pl pt pt_BR ro ru sk sl sv tr ug uk wa zh_CN zh_TW

%define disabled_langs af az be bn_IN bo br csb cy fo fy hne kn ku gu lo mai mi mk ml mt ne oc se si sr ta tg th ven vi xh

%define build_ca_valencia 0

%{expand:%(for lang in %{disabled_langs}; do echo "%%{expand:%%define build_$lang 0}"; done)}
%{expand:%(for lang in %{langlist}; do echo "%%{expand:%%define build_$lang 1}"; done)}

Summary:	Internationalization support for KDE
Name:		kde-l10n
Version:	16.04.0
Release:	2
Epoch:		3
License:	LGPLv2+
Group:		System/Internationalization
Url:		http://www.kde.org
# l10n sources
# list ca@valencia tarball separately due to the @ in the tarball name
#Source1: kde-l10n-ca@valencia-%{version}.tar.xz
%{expand:%(\
    i=2; \
    for lang in %langlist; do\
        echo "%%{expand:Source$i: http://download.kde.org/stable/applications/%%{version}/src/%%{name}/%%{name}-$lang-%%{version}.tar.xz}";\
        i=$[i+1];\
    done\
    )
}
Source100:	kde-l10n.rpmlintrc
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd45-xml
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildArch:	noarch

%description
Internationalization support for KDE.

#----------------------------------------------------------------------------------------

%package en_US
Summary:	American English support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-en
Provides:	%{name}-American = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description en_US
%{summary}.

This is an empty package, en_US support is already provided by KF5.

%files en_US

#----------------------------------------------------------------------------------------

%if %{build_af}
%package af
Summary:	Afrikaans language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Afrikaans = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description af
This package provides Afrikaans translations for KDE.

%files af
%lang(af) %{_datadir}/locale/af/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_ar}
%package ar
Summary:	Arabic language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ar
Provides:	%{name}-Arabic = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ar
This package provides Arabic translation for KDE.

%files ar
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*
%{_datadir}/klettres/ar/
%endif

#----------------------------------------------------------------------------------------

%if %{build_az}
%package az
Summary:	Azerbaijani language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Azerbaijani = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description az
This package provides Azerbaijani translations for KDE.

%files az
%lang(az) %{_datadir}/locale/az/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_be}
%package be
Summary:	Belarusian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Belarusian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description be
%{summary}.

%files be
%lang(be) %{_datadir}/locale/be/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_bn_IN}
%package bn_IN
Summary:	Bengali India language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-bn
Provides:	%{name}-Bengali-India = %{version}-%{release}
Provides:	%{name}-Bengali = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description bn_IN
%{summary}.

%files bn_IN
%lang(bn_IN) %{_datadir}/locale/bn_IN/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_bg}
%package bg
Summary:	Bulgarian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-bg
Provides:	%{name}-Bulgarian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description bg
%{summary}.

%files bg
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/*
%{_datadir}/apps/kvtml/bg/
%endif

#----------------------------------------------------------------------------------------

%if %{build_bo}
%package bo
Summary:	Tibetan language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Tibetan = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description bo
%{summary}.

%files bo
%lang(bo) %{_datadir}/locale/bo/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_br}
%package br
Summary:	Breton language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Breton = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description br
%{summary}.

%files br
%lang(br) %{_datadir}/locale/br/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_bs}
%package bs
Summary:	Bosnian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Bosnian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description bs
%{summary}.

%files bs
%lang(bs) %{_datadir}/locale/bs/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_ca}
%package ca
Summary:	Catalan language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ca
Provides:	%{name}-Catalan = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ca
%{summary}.

%files ca
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/*
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/*
%{_datadir}/khangman/ca.txt
%{_datadir}/ktuberling/sounds/ca.soundtheme
%{_datadir}/ktuberling/sounds/ca/*
%{_datadir}/apps/kvtml/ca/
%{_docdir}/HTML/ca/*
%{_mandir}/ca/man1/*
%{_mandir}/ca/man6/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_ca_valencia}
%package ca-valencia
Summary:	Catalan (Valencian) language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Catalan-Valencian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ca-valencia
%{summary}.

%files ca-valencia
%lang(ca-valencia) %{_datadir}/locale/ca@valencia/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_cs}
%package cs
Summary:	Czech language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-cs
Provides:	%{name}-Czech = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description cs
%{summary}.

%files cs
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*
%{_datadir}/khangman/cs.txt
%{_datadir}/klettres/cs/
%{_datadir}/apps/kvtml/cs/
%{_docdir}/HTML/cs/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_csb}
%package csb
Summary:	Kashubian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-pl
Provides:	%{name}-Kashubian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description csb
%{summary}.

%files csb
%lang(csb) %{_datadir}/locale/csb/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_cy}
%package cy
Summary:	Welsh language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Welsh = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description cy
%{summary}.

%files cy
%lang(cy) %{_datadir}/locale/cy/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_da}
%package da
Summary:	Danish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-da
Provides:	%{name}-Danish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description da
%{summary}.

%files da
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*
%{_docdir}/HTML/da/umbrello
%{_datadir}/khangman/da.txt
%{_datadir}/klettres/da/
%{_datadir}/ktuberling/sounds/da.soundtheme
%{_datadir}/ktuberling/sounds/da/*
%{_datadir}/apps/kvtml/da/
%{_mandir}/da/man1/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_de}
%package de
Summary:	German language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-de
Provides:	%{name}-German = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description de
%{summary}.

%files de
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%{_datadir}/klettres/de/
%{_datadir}/khangman/de.txt
%{_datadir}/apps/kvtml/de/
%{_datadir}/ktuberling/sounds/de.soundtheme
%{_datadir}/ktuberling/sounds/de/*
%{_docdir}/HTML/de/*
%{_mandir}/de/man1/*
%{_mandir}/de/man6/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_el}
%package el
Summary:	Greek language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-el
Provides:	%{name}-Greek = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description el
%{summary}.

%files el
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*
%{_datadir}/apps/kvtml/el
%{_datadir}/ktuberling/sounds/el.soundtheme
%{_datadir}/ktuberling/sounds/el/*
%{_docdir}/HTML/el/
%endif

#----------------------------------------------------------------------------------------

%if %{build_eu}
%package eu
Summary:	Basque language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-eu
Provides:	%{name}-Basque = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description eu
This package provides Basque translations for KDE.

%files eu
%lang(eu) %{_datadir}/locale/eu/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_en_GB}
%package en_GB
Summary:	British English support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-en
Provides:	%{name}-British = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description en_GB
%{summary}.

%files en_GB
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/*
%{_datadir}/klettres/en_GB/
%{_datadir}/apps/kvtml/en_GB/
%{_datadir}/katepart/syntax/logohighlightstyle.en_GB.xml
%{_datadir}/kturtle/data/logokeywords.en_GB.xml
%{_datadir}/kturtle/examples/en_GB/
%endif

#----------------------------------------------------------------------------------------

%if %{build_eo}
%package eo
Summary:	Esperanto support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-eo
Provides:	%{name}-Esperanto = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description eo
%{summary}.

%files eo
%lang(eo) %{_datadir}/locale/eo/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_es}
%package es
Summary:	Spanish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-es
Provides:	%{name}-Spanish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description es
%{summary}.

%files es
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%{_datadir}/khangman/es.txt
%{_datadir}/klettres/es/
%{_datadir}/apps/kvtml/es/
%{_datadir}/ktuberling/sounds/es.soundtheme
%{_datadir}/ktuberling/sounds/es/*
%{_docdir}/HTML/es/*
%{_mandir}/es/man1/*
%{_mandir}/es/man6/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_et}
%package et
Summary:	Estonian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-et
Provides:	%{name}-Estonian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description et
%{summary}.

%files et
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/*
%{_datadir}/khangman/et.txt
%{_datadir}/apps/kvtml/et/
%{_docdir}/HTML/et/*
%{_mandir}/et/man1/*
%{_mandir}/et/man6/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_fa}
%package fa
Summary:	Farsi language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-fa
Provides:	%{name}-Farsi = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description fa
%{summary}.

%files fa
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_fi}
%package fi
Summary:	Finnish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-fi
Provides:	%{name}-Finnish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description fi
%{summary}.

%files fi
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/*
%{_datadir}/locale/fi/LC_SCRIPTS/
%{_datadir}/khangman/fi.txt
%{_datadir}/apps/kvtml/fi/
%{_datadir}/ktuberling/sounds/fi.soundtheme
%{_datadir}/ktuberling/sounds/fi/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_fo}
%package fo
Summary:	Faroese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Faroese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description fo
%{summary}.

%files fo
%lang(fo) %{_datadir}/locale/fo/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_fr}
%package fr
Summary:	French language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-fr
Provides:	%{name}-French = %{version}-%{release}
Conflicts:	nepomuk-scribo < 1:0.6.1-1
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description fr
%{summary}.

%files fr
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%{_datadir}/locale/fr/LC_SCRIPTS/
%{_datadir}/khangman/fr.txt
%{_datadir}/apps/kvtml/fr/
%{_datadir}/kstars/fr/*.dat
%{_docdir}/HTML/fr/*
%{_datadir}/ktuberling/sounds/fr.soundtheme
%{_datadir}/ktuberling/sounds/fr/*
%{_mandir}/fr/man1/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_fy}
%package fy
Summary:	Frisian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-fy
Provides:	%{name}-Frisian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description fy
%{summary}.

%files fy
%lang(fy) %{_datadir}/locale/fy/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_ga}
%package ga
Summary:	Irish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ga
Provides:	%{name}-Irish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ga
%{summary}.

%files ga
%lang(ga) %{_datadir}/locale/ga/LC_MESSAGES/*
%{_datadir}/khangman/ga.txt
%{_datadir}/apps/kvtml/ga/
%{_datadir}/ktuberling/sounds/ga.soundtheme
%{_datadir}/ktuberling/sounds/ga/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_gl}
%package gl
Summary:	Galician language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-gl
Provides:	%{name}-Galician = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description gl
%{summary}.

%files gl
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/*
%{_datadir}/khangman/gl.txt
%{_datadir}/apps/kvtml/gl/
%{_docdir}/HTML/gl/*
%{_datadir}/ktuberling/sounds/gl.soundtheme
%{_datadir}/ktuberling/sounds/gl/*
%{_mandir}/gl/man1/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_gu}
%package gu
Summary:	Gujarati language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-gu
Provides:	%{name}-Gujarati = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description gu
%{summary}.

%files gu
%lang(gu) %{_datadir}/locale/gu/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_he}
%package he
Summary:	Hebrew language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-he
Provides:	%{name}-Hebrew = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description he
%{summary}.

%files he
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/*
%{_datadir}/klettres/he/
%endif

#----------------------------------------------------------------------------------------

%if %{build_hi}
%package hi
Summary:	Hindi language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-hi
Provides:	%{name}-Hindi = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description hi
%{summary}.

%files hi
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_hne}
%package hne
Summary:	Chhattisgarhi language support for KDE 
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-hne
Provides:	%{name}-Chhattisgarhi = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description hne
%{summary}.

%files hne
%lang(hne) %{_datadir}/locale/hne/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_hr}
%package hr
Summary:	Croatian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-hr
Provides:	%{name}-Croatian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description hr
%{summary}.

%files hr
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_hu}
%package hu
Summary:	Hungarian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-hu
Provides:	%{name}-Hungarian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description hu
%{summary}.

%files hu
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*
%{_datadir}/khangman/hu.txt
%{_datadir}/apps/kvtml/hu/
%{_datadir}/klettres/hu/
%endif

#----------------------------------------------------------------------------------------

%if %{build_ia}
%package ia
Summary:	Interlingua language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Interlingua = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ia
%{summary}.

%files ia
%lang(ia) %{_datadir}/locale/ia/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_id}
%package id
Summary:	Indonesian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-id
Provides:	%{name}-Indonesian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description id
%{summary}.

%files id
%lang(id) %{_datadir}/locale/id/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_is}
%package is
Summary:	Icelandic language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-is
Provides:	%{name}-Icelandic = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description is
%{summary}.

%files is
%lang(is) %{_datadir}/locale/is/LC_MESSAGES/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_it}
%package it
Summary:	Italian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-it
Provides:	%{name}-Italian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description it
%{summary}.

%files it
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*
%{_datadir}/klettres/it/
%{_datadir}/apps/kvtml/it/
%{_datadir}/ktuberling/sounds/it.soundtheme
%{_datadir}/ktuberling/sounds/it/*
%{_docdir}/HTML/it/*
%{_mandir}/it/man1/*
%{_mandir}/it/man6/*
%endif

#------------------------------------------------------------------------------

%if %{build_ja}
%package ja
Summary:	Japanese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ja
Provides:	%{name}-Japanese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ja
%{summary}.

%files ja
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*
%{_datadir}/locale/ja/LC_SCRIPTS/
%{_docdir}/HTML/ja/*
%endif

#------------------------------------------------------------------------------

%if %{build_kn}
%package kn
Summary:	Kannada language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-kn
Provides:	%{name}-Kannada = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description kn
%{summary}.

%files kn
%lang(kn) %{_datadir}/locale/kn/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_kk}
%package kk
Summary:	Kazakh language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-kk
Provides:	%{name}-Kazakh = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description kk
%{summary}.

%files kk
%lang(kk) %{_datadir}/locale/kk/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_km}
%package km
Summary:	Khmer language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-km
Provides:	%{name}-Khmer = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description km
%{summary}.

%files km
%lang(km) %{_datadir}/locale/km/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_ko}
%package ko
Summary:	Korean language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ko
Provides:	%{name}-Korean = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ko
%{summary}.

%files ko
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_ku}
%package ku
Summary:	Kurdish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ku
Provides:	%{name}-Kurdish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ku
%{summary}.


%files ku
%lang(ku) %{_datadir}/locale/ku/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_lo}
%package lo
Summary:	Lao language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Lao = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description lo
%{summary}.

%files lo
%lang(lo) %{_datadir}/locale/lo/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_lt}
%package lt
Summary:	Lithuanian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-lt
Provides:	%{name}-Lithuanian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description lt
%{summary}.

%files lt
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/*
%{_datadir}/klettres/lt/
%{_datadir}/klettres/lt.txt
%{_datadir}/ktuberling/sounds/lt.soundtheme
%{_datadir}/ktuberling/sounds/lt/*
%{_docdir}/HTML/lt/*
%endif

#------------------------------------------------------------------------------

%if %{build_lv}
%package lv
Summary:	Latvian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-lv
Provides:	%{name}-Latvian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description lv
%{summary}.

%files lv
%lang(lv) %{_datadir}/locale/lv/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_mi}
%package mi
Summary:	Maori language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Maori = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description mi
%{summary}.

%files mi
%lang(mi) %{_datadir}/locale/mi/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_mk}
%package mk
Summary:	Macedonian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-mk
Provides:	%{name}-Macedonian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description mk
%{summary}.

%files mk
%lang(mk) %{_datadir}/locale/mk/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_mai}
%package mai
Summary:	Maithili language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-mai
Provides:	%{name}-Maithili = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description mai
%{summary}.

%files mai
%lang(mai) %{_datadir}/locale/mai/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_ml}
%package ml
Summary:	Malayalam language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ml
Provides:	%{name}-Malayalam = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ml
%{summary}.

%files ml
%lang(ml) %{_datadir}/locale/ml/LC_MESSAGES/*
%{_datadir}/klettres/ml/
%endif

#------------------------------------------------------------------------------

%if %{build_mt}
%package mt
Summary:	Maltese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Maltese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description mt
%{summary}.

%files mt
%lang(mt) %{_datadir}/locale/mt/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_mr}
%package mr
Summary:	Marathi language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ca
Provides:	%{name}-Marathi = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description mr
%{summary}.

%files mr
%lang(mr) %{_datadir}/locale/mr/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_nb}
%package nb
Summary:	Norwegian (Bokmaal) language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-nb
Provides:	%{name}-Norwegian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description nb
%{summary}.

%files nb
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/*
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/*
%{_datadir}/khangman/nb.txt
%{_datadir}/apps/kvtml/nb/
%{_datadir}/klettres/nb/
%{_datadir}/katepart/syntax/logohighlightstyle.nb.xml
%{_datadir}/kturtle/data/logokeywords.nb.xml
%{_datadir}/kturtle/examples/nb/*.logo
%endif

#------------------------------------------------------------------------------

%if %{build_nds}
%package nds
Summary:	Low Saxon language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-nds
Provides:	%{name}-LowSaxon = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description nds
%{summary}.

%files nds
%lang(nds) %{_datadir}/locale/nds/LC_MESSAGES/*
%{_datadir}/klettres/nds/
%{_datadir}/khangman/nds.txt
%{_datadir}/apps/kvtml/nds/
%{_datadir}/katepart/syntax/logohighlightstyle.nds.xml
%{_datadir}/kturtle/examples/nds
%{_datadir}/kstars/nds/*.dat
%{_datadir}/ktuberling/sounds/nds.soundtheme
%{_datadir}/ktuberling/sounds/nds/*
%endif

#------------------------------------------------------------------------------

%if %{build_ne}
%package ne
Summary:	Nepali language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ne
Provides:	%{name}-Nepali = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ne
%{summary}.

%files ne
%lang(ne) %{_datadir}/locale/ne/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_nl}
%package nl
Summary:	Dutch language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-nl
Provides:	%{name}-nl = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description nl
%{summary}.

%files nl
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*
%{_datadir}/klettres/nl/
%{_datadir}/apps/kvtml/nl/
%{_datadir}/katepart/syntax/logohighlightstyle.nl.xml
%{_datadir}/kturtle/data/logokeywords.nl.xml
%{_datadir}/kturtle/examples/nl/*.logo
%{_datadir}/ktuberling/sounds/nl.soundtheme
%{_datadir}/ktuberling/sounds/nl/*
%{_docdir}/HTML/nl/*
%{_mandir}/nl/man1/*
%{_mandir}/nl/man6/*
%endif

#------------------------------------------------------------------------------

%if %{build_nn}
%package nn
Summary:	Norwegian (Nynorsk) language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-nn
Provides:	%{name}-Norwegian-Nynorsk = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description nn
%{summary}.

%files nn
%lang(nn) %{_datadir}/locale/nn/LC_MESSAGES/*
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/*
%{_datadir}/khangman/nn.txt
%{_datadir}/apps/kvtml/nn/
%{_docdir}/HTML/nn/*
%endif

#------------------------------------------------------------------------------

%if %{build_oc}
%package oc
Summary:	Occitan language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Occitan = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description oc
%{summary}.

%files oc
%lang(oc) %{_datadir}/locale/oc/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_pl}
%package pl
Summary:	Polish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-pl
Provides:	%{name}-Polish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description pl
%{summary}.

%files pl
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*
%{_datadir}/locale/pl/LC_SCRIPTS/
%{_datadir}/khangman/pl.txt
%{_datadir}/apps/kvtml/pl/
%{_docdir}/HTML/pl/*
%{_mandir}/pl/man1/*
%endif

#------------------------------------------------------------------------------

%if %{build_pt}
%package pt
Summary:	Portuguese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-pt
Provides:	%{name}-Portuguese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description pt
%{summary}.

%files pt
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*
%{_datadir}/khangman/pt.txt
%{_datadir}/apps/kvtml/pt/
%{_datadir}/ktuberling/sounds/pt.soundtheme
%{_datadir}/ktuberling/sounds/pt/*
%{_docdir}/HTML/pt/*
%{_mandir}/pt/man1/*
%{_mandir}/pt/man6/*
%endif

#------------------------------------------------------------------------------

%if %{build_pa}
%package pa
Summary:	Punjabi language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-pa
Provides:	%{name}-Punjabi = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description pa
%{summary}.

%files pa
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/*
%{_datadir}/apps/kvtml/pa
%endif

#------------------------------------------------------------------------------

%if %{build_pt_BR}
%package pt_BR
Summary:	Brazil Portuguese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-pt
Provides:	%{name}-Brazil = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description pt_BR
%{summary}.

%files pt_BR
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*
%{_datadir}/autocorrect/pt_BR.xml
%{_datadir}/khangman/pt_BR.txt
%{_datadir}/klettres/pt_BR/*
%{_datadir}/apps/kvtml/pt_BR/
%{_docdir}/HTML/pt_BR/*
%{_mandir}/pt_BR/man1/*
%{_mandir}/pt_BR/man6/*
%endif

#------------------------------------------------------------------------------

%if %{build_ro}
%package ro
Summary:	Romanian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ro
Provides:	%{name}-Romanian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ro
%{summary}.

%files ro
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/*
%{_datadir}/apps/kvtml/ro/
%{_datadir}/ktuberling/sounds/ro.soundtheme
%{_datadir}/ktuberling/sounds/ro/*
%endif

#------------------------------------------------------------------------------

%if %{build_ru}
%package ru
Summary:	Russian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ru
Provides:	%{name}-Russian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ru
%{summary}.

%files ru
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
#%{_datadir}/locale/ru/LC_SCRIPTS/
%{_datadir}/apps/kvtml/ru/
%{_datadir}/katepart/syntax/logohighlightstyle.ru.xml
%{_datadir}/klettres/ru
%{_datadir}/ktuberling/sounds/ru.soundtheme
%{_datadir}/ktuberling/sounds/ru/*
%{_docdir}/HTML/ru/*
%{_mandir}/ru/man1/*
%{_mandir}/ru/man6/*
%endif

#------------------------------------------------------------------------------

%if %{build_se}
%package se
Summary:	Northern Sami language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-se
Provides:	%{name}-NorthernSami = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description se
%{summary}.

%files se
%lang(se) %{_datadir}/locale/se/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_si}
%package si
Summary:	Sinhala language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-si
Provides:	%{name}-Sinhala = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description si
%{summary}.

%files si
%lang(si) %{_datadir}/locale/si/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_sk}
%package sk
Summary:	Slovak language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-sk
Provides:	%{name}-Slovak = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description sk
%{summary}.

%files sk
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_sl}
%package sl
Summary:	Slovenian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-sl
Provides:	%{name}-Slovenian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description sl
%{summary}.

%files sl
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/*
%{_datadir}/khangman/sl.txt
%{_datadir}/apps/kvtml/sl/*
%{_datadir}/ktuberling/sounds/sl.soundtheme
%{_datadir}/ktuberling/sounds/sl/*
%endif

#------------------------------------------------------------------------------

%if %{build_sr}
%package sr
Summary:	Serbian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-sr
Provides:	%{name}-Serbian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description sr
%{summary}.

%files sr
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/*
%{_datadir}/locale/sr/LC_SCRIPTS/
%{_datadir}/locale/sr@latin/LC_MESSAGES/*
%{_datadir}/locale/sr@latin/LC_SCRIPTS/
%{_datadir}/locale/sr@ijekavian/LC_MESSAGES/
%{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/
%{_datadir}/locale/sr@ijekavianlatin/LC_MESSAGES/
%{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS
%{_datadir}/apps/desktoptheme/*/widgets/l10n/sr
%{_datadir}/apps/desktoptheme/*/widgets/l10n/sr@latin
%{_datadir}/apps/desktoptheme/*/widgets/l10n/sr@ijekavian
%{_datadir}/apps/desktoptheme/*/widgets/l10n/sr@ijekavianlatin
%{_datadir}/apps/desktoptheme/default/icons/l10n/sr*
%{_datadir}/khangman/sr@latin.txt
%{_datadir}/apps/kvtml/sr*/
%{_docdir}/HTML/sr/*
%{_docdir}/HTML/sr@latin/*
%endif

#------------------------------------------------------------------------------

%if %{build_sv}
%package sv
Summary:	Swedish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-sv
Provides:	%{name}-Swedish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description sv
%{summary}.

%files sv
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*
%{_datadir}/khangman/sv.txt
%{_datadir}/apps/kvtml/sv/
%{_datadir}/ktuberling/sounds/sv.soundtheme
%{_datadir}/ktuberling/sounds/sv/*
%{_docdir}/HTML/sv/*
%{_mandir}/sv/man1/*
%{_mandir}/sv/man6/*
%endif

#------------------------------------------------------------------------------

%if %{build_ta}
%package ta
Summary:	Tamil language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ta
Provides:	%{name}-Tamil = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ta
%{summary}.

%files ta
%lang(ta) %{_datadir}/locale/ta/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_tg}
%package tg
Summary:	Tajik language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-tg
Provides:	%{name}-Tajik = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description tg
%{summary}.

%files tg
%lang(tg) %{_datadir}/locale/tg/LC_MESSAGES/*
%{_datadir}/apps/kvtml/tg/
%{_datadir}/khangman/tg.txt
%endif

#------------------------------------------------------------------------------

%if %{build_th}
%package th
Summary:	Thai language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-th
Provides:	%{name}-Thai = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description th
%{summary}.

%files th
%lang(th) %{_datadir}/locale/th/LC_MESSAGES/*
%{_datadir}/locale/th/charset
%{_datadir}/locale/th/flag.png
%endif

#------------------------------------------------------------------------------

%if %{build_tr}
%package tr
Summary:	Turkish language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-tr
Provides:	%{name}-Turkish = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description tr
%{summary}.

%files tr
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/*
%{_datadir}/khangman/tr.txt
%{_datadir}/apps/kvtml/tr/
%{_docdir}/HTML/tr/*
%{_mandir}/tr/man1/*
%endif

#------------------------------------------------------------------------------

%if %{build_uk}
%package uk
Summary:	Ukrainian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-uk
Suggests:	%{name}-uk
Provides:	%{name}-Ukrainian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description uk
%{summary}.

%files uk
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*
%{_datadir}/locale/uk/LC_SCRIPTS/
%{_datadir}/apps/kvtml/uk/
%{_datadir}/klettres/uk/
%{_datadir}/ktuberling/sounds/uk.soundtheme
%{_datadir}/ktuberling/sounds/uk/*
%{_docdir}/HTML/uk/*
%{_mandir}/uk/man1/*
%{_mandir}/uk/man6/*
%endif

#------------------------------------------------------------------------------

%if %{build_ug}
%package ug
Summary:	Uyghur language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-ug
Provides:	%{name}-Uyghur = %{version}-%{release}

%description ug
%{summary}.

%files ug
%lang(ug) %{_datadir}/locale/ug/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_ven}
%package ven
Summary:	Venda language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Venda = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description ven
%{summary}.

%files ven
%lang(ven) %{_datadir}/locale/ven/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_vi}
%package vi
Summary:	Vietnamese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Vietnamese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description vi
%{summary}.

%files vi
%lang(vi) %{_datadir}/locale/vi/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_wa}
%package wa
Summary:	Walloon language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-wa
Provides:	%{name}-Walloon = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description wa
%{summary}.

%files wa
%lang(wa) %{_datadir}/locale/wa/LC_MESSAGES/*
%{_datadir}/ktuberling/sounds/wa.soundtheme
%{_datadir}/ktuberling/sounds/wa/*
%endif

#------------------------------------------------------------------------------

%if %{build_xh}
%package xh
Summary:	Xhosa (a Bantu language) support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Xhosa = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description xh
%{summary}.

%files xh
%lang(xh) %{_datadir}/locale/xh/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%if %{build_zh_CN}
%package zh_CN
Summary:	Chinese (Simplified Chinese) language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-zh
Provides:	%{name}-Chinese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description zh_CN
%{summary}.

%files zh_CN
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*
%{_datadir}/apps/kvtml/zh_CN/
%endif

#------------------------------------------------------------------------------

%if %{build_zh_TW}
%package zh_TW
Summary:	Chinese (Traditional) language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Requires:	locales-zh
Provides:	%{name}-Chinese-Traditional = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1
Conflicts:	khelpcenter < 16.04.0

%description zh_TW
%{summary}.

%files zh_TW
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*
%endif

#------------------------------------------------------------------------------

%prep
%setup -T -q -n %{name}-%{version} -c

for lang in %{langlist} ; do
  echo $lang | grep -v '^#' && \
  xz -dc %{_sourcedir}/%{name}-$lang-%{version}.tar.xz | tar -xf -
done

%if %{build_ca_valencia}
tar -xf %{_sourcedir}/%{name}-ca@valencia-%{version}.tar.xz
%endif

%build
for lang in %{langlist} ; do
pushd %{name}-$lang-%{version}
      sed -i /"add_subdirectory(4)"/d CMakeLists.txt
      %cmake_kde5
      %ninja
popd
done

# build ca@valencia separately due to the @ in the tarball name
%if %{build_ca_valencia}
pushd %{name}-ca@valencia-%{version}
      %cmake_kde5
      %ninja
popd
%endif

%install
for lang in %{langlist} ; do
pushd %{name}-$lang-%{version}
     %ninja_install -C build
popd
done

# install ca@valencia separately due to the @ in the tarball name
%if %{build_ca_valencia}
pushd %{name}-ca@valencia-%{version}
     %ninja_install -C build
popd
%endif
