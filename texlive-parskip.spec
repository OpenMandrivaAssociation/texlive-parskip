Name:		texlive-parskip
Version:	58358
Release:	2
Summary:	Layout with zero \parindent, non-zero \parskip
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/parskip
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Simply changing \parskip and \parindent leaves a layout that is
untidy; this package (though it is no substitute for a
properly-designed class) helps alleviate this untidiness.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parskip
%doc %{_texmfdistdir}/doc/latex/parskip

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
