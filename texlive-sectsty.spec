# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sectsty
# catalog-date 2007-01-14 15:20:52 +0100
# catalog-license lppl
# catalog-version 2.0.2
Name:		texlive-sectsty
Version:	2.0.2
Release:	2
Summary:	Control sectional headers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sectsty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectsty.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectsty.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectsty.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX2e package to help change the style of any or all of
LaTeX's sectional headers in the article, book, or report
classes. Examples include the addition of rules above or below
a section title.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sectsty/sectsty.sty
%doc %{_texmfdistdir}/doc/latex/sectsty/sectsty.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sectsty/sectsty.dtx
%doc %{_texmfdistdir}/source/latex/sectsty/sectsty.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
