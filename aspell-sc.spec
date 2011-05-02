%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.0

%define languageenglazy Sardinian
%define languagecode sc
%define lc_ctype sc_IT

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.1
Release:       %mkrel 11
Group:         System/Internationalization
#Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell5-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}


BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
#%setup -q -n %{name}-%{src_ver}
%setup -q -n aspell5-%{languagecode}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

#mv -f README README.%{languagecode}
chmod 644 Copyright README* doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*


