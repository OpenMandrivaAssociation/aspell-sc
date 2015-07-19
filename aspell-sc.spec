%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.0
%define languageenglazy Sardinian
%define languagecode sc
%define lc_ctype sc_IT

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.1
Release:	21
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell5-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn aspell5-%{languagecode}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

#mv -f README README.%{languagecode}
chmod 644 Copyright README* doc/*

%files
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*

