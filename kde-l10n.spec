# Supported l10n language
# to update this list (depending on which new localisations tarballs are available
# from upstream), you can use:
# $ ls SOURCES/kde-l10n*tar.bz2 | grep -v @valencia | awk -F- '{print $3}' | tr '\n' ' '
#
# Note: ca@valencia is treated differently because of the @ in the tarball name
%define langlist ar bg bs ca cs da de el en_GB es et eu fa fi fr ga gl he hr hu ia is it ja kk km ko lt lv nb nds nl nn pa pl pt pt_BR ro ru si sk sl sv th tr ug uk wa zh_CN zh_TW

%define disabled_langs af az be bn_IN bo br csb cy eo fo fy hne kn ku gu hi id lo mai mi mk ml mt mr ne se oc sr ta tg ven vi xh

%define build_ca_valencia 0

#%{expand:%(for lang in %{disabled_langs}; do echo "%%{expand:%%define build_$lang 0"}; done)}
#%{expand:%(for lang in %{langlist}; do echo "%%{expand:%%define build_$lang 1"}; done)}
%{expand:%(for lang in %{disabled_langs}; do echo "%%{expand:%%define build_$lang 0}"; done)}
%{expand:%(for lang in %{langlist}; do echo "%%{expand:%%define build_$lang 1}"; done)}

Name:		kde-l10n
Version:	4.10.0
Release:	1
Epoch:		3
Url:		http://www.kde.org
Summary:	Internationalization support for KDE
Group:		System/Internationalization
License:	LGPLv2
BuildArch:	noarch
# l10n sources
# list ca@valencia tarball separately due to the @ in the tarball name
#Source1: kde-l10n-ca@valencia-%{version}.tar.bz2
%{expand:%(\
    i=2; \
    for lang in %langlist; do\
        echo "%%{expand:Source$i: ftp://ftp.kde.org/pub/kde/stable/%%{version}/src/%%{name}/%%{name}-$lang-%%{version}.tar.xz}";\
        i=$[i+1];\
    done\
    )
}
Source100:	kde-l10n.rpmlintrc
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd42-xml
BuildRequires:	kdelibs4-devel >= %{version}

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

%description en_US
%{summary}.

This is an empty package, en_US support is already provided by kdelibs4.

%files en_US

#----------------------------------------------------------------------------------------

%if %{build_af}
%package af
Summary:	Afrikaans language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Afrikaans = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description af
This package provides Afrikaans translations for KDE.

%files af
%lang(af) %{_kde_datadir}/locale/af/LC_MESSAGES/*
%{_kde_datadir}/locale/af/entry.desktop
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

%description ar
This package provides Arabic translation for KDE.

%files ar
%lang(ar) %{_kde_datadir}/locale/ar/LC_MESSAGES/*
%{_kde_datadir}/locale/ar/entry.desktop
%{_kde_datadir}/locale/ar/LC_SCRIPTS/
%{_kde_appsdir}/klettres/ar/
%endif

#----------------------------------------------------------------------------------------

%if %{build_az}
%package az
Summary:	Azerbaijani language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Azerbaijani = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description az
This package provides Azerbaijani translations for KDE.

%files az
%lang(az) %{_kde_datadir}/locale/az/LC_MESSAGES/*
%{_kde_datadir}/locale/az/entry.desktop
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

%description eu
This package provides Basque translations for KDE.


%files eu
%lang(eu) %{_kde_datadir}/locale/eu/LC_MESSAGES/*
%{_kde_datadir}/locale/eu/entry.desktop
%{_kde_docdir}/HTML/eu/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_be}
%package be
Summary:	Belarusian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Belarusian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description be
%{summary}.

%files be
%lang(be) %{_kde_datadir}/locale/be/LC_MESSAGES/*
%{_kde_datadir}/locale/be/entry.desktop
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

%description bn_IN
%{summary}.

%files bn_IN
%lang(bn_IN) %{_kde_datadir}/locale/bn_IN/LC_MESSAGES/*
%{_kde_datadir}/locale/bn_IN/entry.desktop
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
%description bg
%{summary}.

%files bg
%lang(bg) %{_kde_datadir}/locale/bg/LC_MESSAGES/*
%{_kde_datadir}/locale/bg/entry.desktop
%{_kde_appsdir}/kvtml/bg/
%endif

#----------------------------------------------------------------------------------------

%if %{build_bo}
%package bo
Summary:	Tibetan language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Tibetan = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description bo
%{summary}.

%files bo
%lang(bo) %{_kde_datadir}/locale/bo/LC_MESSAGES/*
%{_kde_datadir}/locale/bo/entry.desktop
%endif

#----------------------------------------------------------------------------------------

%if %{build_br}
%package br
Summary:	Breton language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Breton = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description br
%{summary}.

%files br
%lang(br) %{_kde_datadir}/locale/br/LC_MESSAGES/*
%{_kde_datadir}/locale/br/entry.desktop
%endif

#----------------------------------------------------------------------------------------

%if %{build_bs}
%package bs
Summary:	Bosnian language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Bosnian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description bs
%{summary}.

%files bs
%lang(bs) %{_kde_datadir}/locale/bs/LC_MESSAGES/*
%{_kde_datadir}/locale/bs/entry.desktop
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

%description ca
%{summary}.

%files ca
%lang(ca) %{_kde_datadir}/locale/ca/LC_MESSAGES/*
%{_kde_datadir}/locale/ca/LC_SCRIPTS/
%{_kde_datadir}/locale/ca/entry.desktop
%{_kde_appsdir}/khangman/ca.txt
%{_kde_appsdir}/ktuberling/sounds/ca*
%{_kde_appsdir}/kvtml/ca/
%{_kde_docdir}/HTML/ca/*
%{_kde_mandir}/ca/*/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_ca_valencia}
%package ca-valencia
Summary:	Catalan (Valencian) language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Catalan-Valencian = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description ca-valencia
%{summary}.

%files ca-valencia
%lang(ca-valencia) %{_kde_datadir}/locale/ca@valencia/LC_MESSAGES/*
%{_kde_datadir}/locale/ca@valencia/entry.desktop
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

%description cs
%{summary}.

%files cs
%lang(cs) %{_kde_datadir}/locale/cs/LC_MESSAGES/*
%{_kde_datadir}/locale/cs/entry.desktop
%{_kde_appsdir}/khangman/cs.txt
%{_kde_appsdir}/klettres/cs/
%{_kde_appsdir}/kvtml/cs/
%{_kde_docdir}/HTML/cs/*
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

%description csb
%{summary}.

%files csb
%lang(csb) %{_kde_datadir}/locale/csb/LC_MESSAGES/*
%{_kde_datadir}/locale/csb/entry.desktop
%endif

#----------------------------------------------------------------------------------------

%if %{build_cy}
%package cy
Summary:	Welsh language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Welsh = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description cy
%{summary}.

%files cy
%lang(cy) %{_kde_datadir}/locale/cy/LC_MESSAGES/*
%{_kde_datadir}/locale/cy/entry.desktop
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

%description da
%{summary}.

%files da
%lang(da) %{_kde_datadir}/locale/da/LC_MESSAGES/*
%{_kde_datadir}/locale/da/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/da*
%{_kde_appsdir}/khangman/da.txt
%{_kde_appsdir}/klettres/da/
%{_kde_appsdir}/kvtml/da/
%{_kde_docdir}/HTML/da/*
%{_kde_mandir}/da/*/*
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

%description de
%{summary}.

%files de
%lang(de) %{_kde_datadir}/locale/de/LC_MESSAGES/*
%{_kde_datadir}/locale/de/LC_SCRIPTS/
%{_kde_datadir}/locale/de/entry.desktop
%{_kde_appsdir}/kajongg/voices/de/
%{_kde_appsdir}/klettres/de/
%{_kde_appsdir}/ktuberling/sounds/de*
%{_kde_appsdir}/khangman/de.txt
%{_kde_appsdir}/kvtml/de/
%{_kde_appsdir}/step/objinfo/l10n/de/
%{_kde_docdir}/HTML/de/*
%{_kde_mandir}/de/*/*
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

%description el
%{summary}.

%files el
%lang(el) %{_kde_datadir}/locale/el/LC_MESSAGES/*
%{_kde_datadir}/locale/el/entry.desktop
%{_kde_appsdir}/kvtml/el
%{_kde_appsdir}/ktuberling/sounds/el*
%{_kde_docdir}/HTML/el/
%{_kde_mandir}/el/*/*
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
%description gu
%{summary}.

%files gu
%lang(gu) %{_kde_datadir}/locale/gu/LC_MESSAGES/*
%{_kde_datadir}/locale/gu/entry.desktop
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

%description en_GB
%{summary}.

%files en_GB
%lang(en_GB) %{_kde_datadir}/locale/en_GB/LC_MESSAGES/*
%{_kde_datadir}/locale/en_GB/entry.desktop
%{_kde_appsdir}/klettres/en_GB/
%{_kde_appsdir}/kvtml/en_GB/
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.en_GB.xml
%{_kde_appsdir}/kturtle/data/logokeywords.en_GB.xml
%{_kde_appsdir}/kturtle/examples/en_GB/
%{_kde_docdir}/HTML/en_GB/
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

%description eo
%{summary}.

%files eo
%lang(eo) %{_kde_datadir}/locale/eo/LC_MESSAGES/*
%{_kde_datadir}/locale/eo/entry.desktop
%{_kde_docdir}/HTML/eo/*
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

%description es
%{summary}.

%files es
%lang(es) %{_kde_datadir}/locale/es/LC_MESSAGES/*
%{_kde_datadir}/locale/es/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/es*
%{_kde_appsdir}/khangman/es.txt
%{_kde_appsdir}/klettres/es/
%{_kde_appsdir}/kvtml/es/
%{_kde_docdir}/HTML/es/*
%{_kde_mandir}/es/*/*
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

%description et
%{summary}.

%files et
%lang(et) %{_kde_datadir}/locale/et/LC_MESSAGES/*
%{_kde_datadir}/locale/et/entry.desktop
%{_kde_appsdir}/khangman/et.txt
%{_kde_appsdir}/kvtml/et/
%{_kde_docdir}/HTML/et/*
%{_kde_mandir}/et/*/*
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

%description fa
%{summary}.

%files fa
%lang(fa) %{_kde_datadir}/locale/fa/LC_MESSAGES/*
%{_kde_datadir}/locale/fa/entry.desktop
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

%description fi
%{summary}.

%files fi
%lang(fi) %{_kde_datadir}/locale/fi/LC_MESSAGES/*
%{_kde_datadir}/locale/fi/entry.desktop
%{_kde_datadir}/locale/fi/LC_SCRIPTS/
%{_kde_appsdir}/khangman/fi.txt
%{_kde_appsdir}/ktuberling/sounds/fi*
%{_kde_appsdir}/kvtml/fi/
%endif

#----------------------------------------------------------------------------------------

%if %{build_fo}
%package fo
Summary:	Faroese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Faroese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description fo
%{summary}.

%files fo
%lang(fo) %{_kde_datadir}/locale/fo/LC_MESSAGES/*
%{_kde_datadir}/locale/fo/entry.desktop
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

%description fr
%{summary}.

%files fr
%lang(fr) %{_kde_datadir}/locale/fr/LC_MESSAGES/*
%{_kde_datadir}/locale/fr/LC_SCRIPTS/
%{_kde_datadir}/locale/fr/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/fr*
%{_kde_appsdir}/khangman/fr.txt
%{_kde_appsdir}/kvtml/fr/
%{_kde_docdir}/HTML/fr/*
%{_kde_mandir}/fr/*/*
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

%description fy
%{summary}.

%files fy
%lang(fy) %{_kde_datadir}/locale/fy/LC_MESSAGES/*
%{_kde_datadir}/locale/fy/entry.desktop
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

%description ga
%{summary}.

%files ga
%lang(ga) %{_kde_datadir}/locale/ga/LC_MESSAGES/*
%{_kde_datadir}/locale/ga/LC_SCRIPTS/
%{_kde_datadir}/locale/ga/entry.desktop
%{_kde_appsdir}/khangman/ga.txt
%{_kde_appsdir}/ktuberling/sounds/ga*
%{_kde_appsdir}/kvtml/ga/
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

%description gl
%{summary}.

%files gl
%lang(gl) %{_kde_datadir}/locale/gl/LC_MESSAGES/*
%{_kde_datadir}/locale/gl/entry.desktop
%{_kde_appsdir}/khangman/gl.txt
%{_kde_appsdir}/kvtml/gl/
%{_kde_appsdir}/ktuberling/sounds/gl.soundtheme
%{_kde_appsdir}/ktuberling/sounds/gl/
%{_kde_docdir}/HTML/gl/*
%{_kde_mandir}/gl/*/*
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

%description he
%{summary}.

%files he
%lang(he) %{_kde_datadir}/locale/he/LC_MESSAGES/*
%{_kde_datadir}/locale/he/entry.desktop
%{_kde_appsdir}/klettres/he/
%{_kde_docdir}/HTML/he/*
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

%description hi
%{summary}.

%files hi
%lang(hi) %{_kde_datadir}/locale/hi/LC_MESSAGES/*
%{_kde_datadir}/locale/hi/entry.desktop
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

%description hne
%{summary}.

%files hne
%lang(hne) %{_kde_datadir}/locale/hne/LC_MESSAGES/*
%{_kde_datadir}/locale/hne/entry.desktop
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

%description hr
%{summary}.

%files hr
%lang(hr) %{_kde_datadir}/locale/hr/LC_MESSAGES/*
%{_kde_datadir}/locale/hr/entry.desktop
%{_kde_datadir}/locale/hr/LC_SCRIPTS
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

%description hu
%{summary}.

%files hu
%lang(hu) %{_kde_datadir}/locale/hu/LC_MESSAGES/*
%{_kde_datadir}/locale/hu/entry.desktop
%{_kde_appsdir}/kanagram/hu.txt
%{_kde_appsdir}/khangman/hu.txt
%{_kde_appsdir}/kvtml/hu/
%{_kde_appsdir}/klettres/hu/
%{_kde_docdir}/HTML/hu/*
%endif

#----------------------------------------------------------------------------------------

%if %{build_ia}
%package ia
Summary:	Interlingua language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Interlingua = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description ia
%{summary}.

%files ia
%lang(ia) %{_kde_datadir}/locale/ia/LC_MESSAGES/*
%{_kde_datadir}/locale/ia/entry.desktop
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

%description id
%{summary}.

%files id
%lang(id) %{_kde_datadir}/locale/id/LC_MESSAGES/*
%{_kde_datadir}/locale/id/entry.desktop
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

%description is
%{summary}.

%files is
%lang(is) %{_kde_datadir}/locale/is/LC_MESSAGES/*
%{_kde_datadir}/locale/is/entry.desktop
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

%description it
%{summary}.

%files it
%lang(it) %{_kde_datadir}/locale/it/LC_MESSAGES/*
%{_kde_datadir}/locale/it/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/it*
%{_kde_appsdir}/klettres/it/
%{_kde_appsdir}/kvtml/it/
%{_kde_appsdir}/step/objinfo/l10n/it/
%{_kde_docdir}/HTML/it/*
%{_kde_mandir}/it/*/*
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

%description ja
%{summary}.

%files ja
%lang(ja) %{_kde_datadir}/locale/ja/LC_MESSAGES/*
%{_kde_datadir}/locale/ja/LC_SCRIPTS/
%{_kde_datadir}/locale/ja/entry.desktop
%{_kde_docdir}/HTML/ja/*
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

%description kn
%{summary}.

%files kn
%lang(kn) %{_kde_datadir}/locale/kn/LC_MESSAGES/*
%{_kde_datadir}/locale/kn/entry.desktop
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

%description kk
%{summary}.

%files kk
%lang(kk) %{_kde_datadir}/locale/kk/LC_MESSAGES/*
%{_kde_datadir}/locale/kk/entry.desktop
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

%description km
%{summary}.

%files km
%lang(km) %{_kde_datadir}/locale/km/LC_MESSAGES/*
%{_kde_datadir}/locale/km/entry.desktop
%{_kde_datadir}/locale/km/flag.png
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

%description ko
%{summary}.

%files ko
%lang(ko) %{_kde_datadir}/locale/ko/LC_MESSAGES/*
%{_kde_datadir}/locale/ko/LC_SCRIPTS/
%{_kde_datadir}/locale/ko/entry.desktop
%{_kde_docdir}/HTML/ko/*
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

%description ku
%{summary}.


%files ku
%lang(ku) %{_kde_datadir}/locale/ku/LC_MESSAGES/*
%{_kde_datadir}/locale/ku/entry.desktop
%endif

#------------------------------------------------------------------------------

%if %{build_lo}
%package lo
Summary:	Lao language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Lao = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description lo
%{summary}.

%files lo
%lang(lo) %{_kde_datadir}/locale/lo/LC_MESSAGES/*
%{_kde_datadir}/locale/lo/entry.desktop
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

%description lt
%{summary}.

%files lt
%lang(lt) %{_kde_datadir}/locale/lt/LC_MESSAGES/*
%{_kde_datadir}/locale/lt/LC_SCRIPTS/
%{_kde_datadir}/locale/lt/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/lt/
%{_kde_appsdir}/ktuberling/sounds/lt.soundtheme
%{_kde_docdir}/HTML/lt/*
%{_kde_mandir}/lt/*/*
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

%description lv
%{summary}.

%files lv
%lang(lv) %{_kde_datadir}/locale/lv/LC_MESSAGES/*
%{_kde_datadir}/locale/lv/entry.desktop
%{_kde_datadir}/locale/lv/LC_SCRIPTS
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

%description nds
%{summary}.

%files nds
%lang(nds) %{_kde_datadir}/locale/nds/LC_MESSAGES/*
%{_kde_datadir}/locale/nds/entry.desktop
%{_kde_appsdir}/klettres/nds/
%{_kde_appsdir}/khangman/nds.txt
%{_kde_appsdir}/kvtml/nds/
%{_kde_appsdir}/ktuberling/sounds/nds*
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.nds.xml
%{_kde_appsdir}/kturtle/examples/nds
%{_kde_docdir}/HTML/nds/*
%endif

#------------------------------------------------------------------------------

%if %{build_mi}
%package mi
Summary:	Maori language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Maori = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description mi
%{summary}.

%files mi
%lang(mi) %{_kde_datadir}/locale/mi/LC_MESSAGES/*
%{_kde_datadir}/locale/mi/entry.desktop
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

%description mk
%{summary}.

%files mk
%lang(mk) %{_kde_datadir}/locale/mk/LC_MESSAGES/*
%{_kde_datadir}/locale/mk/entry.desktop
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

%description mai
%{summary}.

%files mai
%lang(mai) %{_kde_datadir}/locale/mai/LC_MESSAGES/*
%{_kde_datadir}/locale/mai/entry.desktop
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

%description ml
%{summary}.

%files ml
%lang(ml) %{_kde_datadir}/locale/ml/LC_MESSAGES/*
%{_kde_datadir}/locale/ml/LC_SCRIPTS/
%{_kde_datadir}/locale/ml/entry.desktop
%{_kde_appsdir}/klettres/ml/
%endif

#------------------------------------------------------------------------------

%if %{build_mt}
%package mt
Summary:	Maltese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Maltese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description mt
%{summary}.

%files mt
%lang(mt) %{_kde_datadir}/locale/mt/LC_MESSAGES/*
%{_kde_datadir}/locale/mt/entry.desktop
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

%description mr
%{summary}.

%files mr
%lang(mr) %{_kde_datadir}/locale/mr/LC_MESSAGES/*
%{_kde_datadir}/locale/mr/entry.desktop
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

%description ne
%{summary}.

%files ne
%lang(ne) %{_kde_datadir}/locale/ne/LC_MESSAGES/*
%{_kde_datadir}/locale/ne/entry.desktop
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

%description nl
%{summary}.

%files nl
%lang(nl) %{_kde_datadir}/locale/nl/LC_MESSAGES/*
%{_kde_datadir}/locale/nl/LC_SCRIPTS/
%{_kde_datadir}/locale/nl/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/nl*
%{_kde_appsdir}/klettres/nl/
%{_kde_appsdir}/kvtml/nl/
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.nl.xml
%{_kde_appsdir}/kturtle/data/logokeywords.nl.xml
%{_kde_appsdir}/kturtle/examples/nl/*.logo
%{_kde_docdir}/HTML/nl/*
%{_kde_mandir}/nl/*/*
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

%description se
%{summary}.

%files se
%lang(se) %{_kde_datadir}/locale/se/LC_MESSAGES/*
%{_kde_datadir}/locale/se/entry.desktop
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

%description nb
%{summary}.

%files nb
%lang(nb) %{_kde_datadir}/locale/nb/LC_MESSAGES/*
%{_kde_datadir}/locale/nb/LC_SCRIPTS/
%{_kde_datadir}/locale/nb/entry.desktop
%{_kde_appsdir}/khangman/nb.txt
%{_kde_appsdir}/kvtml/nb/
%{_kde_appsdir}/klettres/nb/
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.nb.xml
%{_kde_appsdir}/kturtle/data/logokeywords.nb.xml
%{_kde_appsdir}/kturtle/examples/nb/*.logo
%{_kde_docdir}/HTML/nb/*
%{_kde_mandir}/nb/*/*
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

%description nn
%{summary}.

%files nn
%lang(nn) %{_kde_datadir}/locale/nn/LC_MESSAGES/*
%{_kde_datadir}/locale/nn/LC_SCRIPTS/
%{_kde_datadir}/locale/nn/entry.desktop
%{_kde_appsdir}/khangman/nn.txt
%{_kde_appsdir}/kvtml/nn/
%{_kde_docdir}/HTML/nn/*
%endif

#------------------------------------------------------------------------------

%if %{build_oc}
%package oc
Summary:	Occitan language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Occitan = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description oc
%{summary}.

%files oc
%lang(oc) %{_kde_datadir}/locale/oc/LC_MESSAGES/*
%{_kde_datadir}/locale/oc/entry.desktop
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

%description pl
%{summary}.

%files pl
%lang(pl) %{_kde_datadir}/locale/pl/LC_MESSAGES/*
%{_kde_datadir}/locale/pl/LC_SCRIPTS/
%{_kde_datadir}/locale/pl/entry.desktop
%{_kde_appsdir}/khangman/pl.txt
%{_kde_appsdir}/kvtml/pl/
%{_kde_docdir}/HTML/pl/*
%{_kde_mandir}/pl/*/*
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

%description pt
%{summary}.

%files pt
%lang(pt) %{_kde_datadir}/locale/pt/LC_MESSAGES/*
%{_kde_datadir}/locale/pt/entry.desktop
%{_kde_appsdir}/khangman/pt.txt
%{_kde_appsdir}/ktuberling/sounds/pt*
%{_kde_appsdir}/kvtml/pt/
%{_kde_docdir}/HTML/pt/*
%{_kde_mandir}/pt/*/*
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

%description pa
%{summary}.

%files pa
%lang(pa) %{_kde_datadir}/locale/pa/LC_MESSAGES/*
%{_kde_datadir}/locale/pa/entry.desktop
%{_kde_appsdir}/kvtml/pa
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

%description pt_BR
%{summary}.

%files pt_BR
%lang(pt_BR) %{_kde_datadir}/locale/pt_BR/LC_MESSAGES/*
%{_kde_datadir}/locale/pt_BR/entry.desktop
%{_kde_appsdir}/khangman/pt_BR.txt
%{_kde_appsdir}/klettres/pt_BR/*
%{_kde_appsdir}/kvtml/pt_BR/
%{_kde_docdir}/HTML/pt_BR/*
%{_kde_mandir}/pt_BR/*/*
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

%description ro
%{summary}.

%files ro
%lang(ro) %{_kde_datadir}/locale/ro/LC_MESSAGES/*
%{_kde_datadir}/locale/ro/entry.desktop
%{_kde_appsdir}/kvtml/ro/
%{_kde_appsdir}/ktuberling/sounds/ro*
%{_kde_docdir}/HTML/ro/*
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

%description ru
%{summary}.

%files ru
%lang(ru) %{_kde_datadir}/locale/ru/LC_MESSAGES/*
%{_kde_datadir}/locale/ru/LC_SCRIPTS/
%{_kde_datadir}/locale/ru/entry.desktop
%{_kde_appsdir}/kvtml/ru/
%{_kde_appsdir}/katepart/syntax/logohighlightstyle.ru.xml
%{_kde_appsdir}/klettres/ru
%{_kde_appsdir}/ktuberling/sounds/ru/
%{_kde_appsdir}/ktuberling/sounds/ru.soundtheme
%{_kde_docdir}/HTML/ru/*
%{_kde_mandir}/ru/*/*
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

%description si
%{summary}.

%files si
%lang(si) %{_kde_datadir}/locale/si/LC_MESSAGES/*
%{_kde_datadir}/locale/si/entry.desktop
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

%description sk
%{summary}.

%files sk
%lang(sk) %{_kde_datadir}/locale/sk/LC_MESSAGES/*
%{_kde_datadir}/locale/sk/entry.desktop
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

%description sl
%{summary}.

%files sl
%lang(sl) %{_kde_datadir}/locale/sl/LC_MESSAGES/*
%{_kde_datadir}/locale/sl/entry.desktop
%{_kde_docdir}/HTML/sl/*
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

%description sr
%{summary}.

%files sr
%lang(sr) %{_kde_datadir}/locale/sr/LC_MESSAGES/*
%{_kde_datadir}/locale/sr/LC_SCRIPTS/
%{_kde_datadir}/locale/sr/entry.desktop
%{_kde_datadir}/locale/sr@latin/entry.desktop
%{_kde_datadir}/locale/sr@latin/LC_MESSAGES/*
%{_kde_datadir}/locale/sr@latin/LC_SCRIPTS/
%{_kde_datadir}/locale/sr@ijekavian/LC_MESSAGES/
%{_kde_datadir}/locale/sr@ijekavian/LC_SCRIPTS/
%{_kde_datadir}/locale/sr@ijekavian/entry.desktop
%{_kde_datadir}/locale/sr@ijekavianlatin/LC_MESSAGES/
%{_kde_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS
%{_kde_datadir}/locale/sr@ijekavianlatin/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/sr*
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
%{_kde_docdir}/HTML/sr/*
%{_kde_docdir}/HTML/sr@latin/*
%{_kde_mandir}/sr/*/*
%{_kde_mandir}/sr@latin/*/*
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

%description sv
%{summary}.

%files sv
%lang(sv) %{_kde_datadir}/locale/sv/LC_MESSAGES/*
%{_kde_datadir}/locale/sv/entry.desktop
%{_kde_datadir}/locale/sv/LC_SCRIPTS/
%{_kde_appsdir}/ktuberling/sounds/sv*
%{_kde_appsdir}/khangman/sv.txt
%{_kde_appsdir}/kvtml/sv/
%{_kde_docdir}/HTML/sv/*
%{_kde_mandir}/sv/*/*
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

%description ta
%{summary}.

%files ta
%lang(ta) %{_kde_datadir}/locale/ta/LC_MESSAGES/*
%{_kde_datadir}/locale/ta/entry.desktop
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

%description tg
%{summary}.

%files tg
%lang(tg) %{_kde_datadir}/locale/tg/LC_MESSAGES/*
%{_kde_datadir}/locale/tg/entry.desktop
%{_kde_appsdir}/kvtml/tg/
%{_kde_appsdir}/khangman/tg.txt
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

%description th
%{summary}.

%files th
%lang(th) %{_kde_datadir}/locale/th/LC_MESSAGES/*
%{_kde_datadir}/locale/th/charset
%{_kde_datadir}/locale/th/entry.desktop
%{_kde_datadir}/locale/th/flag.png
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

%description tr
%{summary}.

%files tr
%lang(tr) %{_kde_datadir}/locale/tr/LC_MESSAGES/*
%{_kde_datadir}/locale/tr/entry.desktop
%{_kde_appsdir}/khangman/tr.txt
%{_kde_appsdir}/kvtml/tr/
%{_kde_docdir}/HTML/tr/*
%{_kde_mandir}/tr/*/*
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

%description uk
%{summary}.

%files uk
%lang(uk) %{_kde_datadir}/locale/uk/LC_MESSAGES/*
%{_kde_datadir}/locale/uk/LC_SCRIPTS/
%{_kde_datadir}/locale/uk/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/uk*
%{_kde_appsdir}/step/objinfo/l10n/uk/
%{_kde_appsdir}/kvtml/uk/
%{_kde_appsdir}/klettres/uk/
%{_kde_docdir}/HTML/uk/*
%{_kde_mandir}/uk/*/*
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
%lang(ug) %{_kde_datadir}/locale/ug/LC_MESSAGES/*
%{_kde_datadir}/locale/ug/entry.desktop
%endif

#------------------------------------------------------------------------------

%if %{build_ven}
%package ven
Summary:	Venda language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Venda = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description ven
%{summary}.

%files ven
%lang(ven) %{_kde_datadir}/locale/ven/LC_MESSAGES/*
%{_kde_datadir}/locale/ven/entry.desktop
%endif

#------------------------------------------------------------------------------

%if %{build_vi}
%package vi
Summary:	Vietnamese language support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Vietnamese = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description vi
%{summary}.

%files vi
%lang(vi) %{_kde_datadir}/locale/vi/LC_MESSAGES/*
%{_kde_datadir}/locale/vi/entry.desktop
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

%description wa
%{summary}.

%files wa
%lang(wa) %{_kde_datadir}/locale/wa/LC_MESSAGES/*
%{_kde_datadir}/locale/wa/entry.desktop
%{_kde_appsdir}/ktuberling/sounds/wa*
%{_kde_docdir}/HTML/wa/*
%endif

#------------------------------------------------------------------------------

%if %{build_xh}
%package xh
Summary:	Xhosa (a Bantu language) support for KDE
Group:		System/Internationalization
Provides:	%{name} = %{version}
Provides:	%{name}-Xhosa = %{version}-%{release}
Conflicts:	konq-plugins < 1:4.6.1

%description xh
%{summary}.

%files xh
%lang(xh) %{_kde_datadir}/locale/xh/LC_MESSAGES/*
%{_kde_datadir}/locale/xh/entry.desktop
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

%description zh_CN
%{summary}.

%files zh_CN
%lang(zh_CN) %{_kde_datadir}/locale/zh_CN/LC_MESSAGES/*
%{_kde_datadir}/locale/zh_CN/LC_SCRIPTS/
%{_kde_datadir}/locale/zh_CN/charset
%{_kde_datadir}/locale/zh_CN/entry.desktop
%{_kde_datadir}/locale/zh_CN/flag.png
%{_kde_appsdir}/kvtml/zh_CN/
%{_kde_appsdir}/step/objinfo/l10n/zh_CN/
%{_kde_docdir}/HTML/zh_CN/*
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

%description zh_TW
%{summary}.

%files zh_TW
%lang(zh_TW) %{_kde_datadir}/locale/zh_TW/LC_MESSAGES/*
%{_kde_datadir}/locale/zh_TW/entry.desktop
%{_kde_docdir}/HTML/zh_TW/*
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
      %cmake_kde4
      %make
popd
done

# build ca@valencia separately due to the @ in the tarball name
%if %{build_ca_valencia}
pushd %{name}-ca@valencia-%{version}
      %cmake_kde4
      %make
popd
%endif

%install
for lang in %{langlist} ; do
pushd %{name}-$lang-%{version}
     %makeinstall_std -C build
popd
done

# install ca@valencia separately due to the @ in the tarball name
%if %{build_ca_valencia}
pushd %{name}-ca@valencia-%{version}
     %makeinstall_std -C build
popd
%endif

%changelog
* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0
- Update files for sl

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2
- Update files for fr locale

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Mon Aug 06 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Mon Jul 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- Update to 4.8.95
- Update file list
- Disable kde-l10n-ru-4.8.4-translations patch

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.4-69.1mib2010.2
- New version 4.8.4
- Add kde-l10n-ru-4.8.4-translations patch from Rosa
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.2-69.1mib2010.2
- New version 4.8.2
- Enable pt_BR language
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.1-69.1mib2010.2
- New version 4.8.1
- Enable he, id and ug languages again
- Update file lists for fr and pa packages
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.0-69.1mib2010.2
+ Revision: 762070
- Backport to 2010.2 for MIB users
- Disable missing he, id, kn and ug languages
- MIB (Mandriva International Backports)

* Wed Jan 18 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.97-1
+ Revision: 762070
- Enable fa and si
- Fix uk file list
- Enable pt
- Disable pt translation for now
- New version
- Add back epoch
- Remove Source1
- Disable build_ca_valencia
- Remove %%rename  as kde4-l10n is on not supported anymore distributions
- Remove comments
- Disable build_ca_valencia for now
- Update spec file ( sync with mageia)
- New sources
- New version 4.7.80

  + Zé <ze@mandriva.org>
    - add 4.7.1 sources
    - drop old sources
    - drop old sources

  + vsinitsyn <vsinitsyn>
    - Updated Russian translation for Dolphin, KSysGuard and Nepomuk (this time correct way)
    - Revert commit 696126: Never modify tarball directly
    - Updated Russian translation for Dolphin, KSysGuard and Nepomuk

* Thu Jul 07 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 3:4.6.4-3
+ Revision: 689150
- fix upgrade from 2009.0 by provides/obsoleting kde4-l10n-foo
- use %%global, not %%define (which'll break) for loop in %%{expand:...}

* Mon Jun 27 2011 Alex Burmashev <burmashev@mandriva.org> 3:4.6.4-2
+ Revision: 687462
- updated russian dolphin locale

  + Funda Wang <fwang@mandriva.org>
    - please remove duplicate translations with kdepim

* Tue Jun 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.6.4-1
+ Revision: 685093
- import kde-l10n

