%global tl_name parskip
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0h
Release:	%{tl_revision}.1
Summary:	Layout with zero \parindent, non-zero \parskip
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/parskip
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Simply changing \parskip and \parindent leaves a layout that is untidy;
this package (though it is no substitute for a properly-designed class)
helps alleviate this untidiness.

