Name:		texlive-parskip
Version:	2.0
Release:	1
Summary:	Layout with zero \parindent, non-zero \parskip
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parskip
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Simply changing \parskip and \parindent leaves a layout that is
untidy; this package (though it is no substitute for a
properly-designed class) helps alleviate this untidiness.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parskip/parskip.sty
%doc %{_texmfdistdir}/doc/latex/parskip/parskip-doc.pdf
%doc %{_texmfdistdir}/doc/latex/parskip/parskip-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
