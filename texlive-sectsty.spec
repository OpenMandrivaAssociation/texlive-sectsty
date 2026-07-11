%global tl_name sectsty
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.2
Release:	%{tl_revision}.1
Summary:	Control sectional headers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sectsty
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sectsty.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sectsty.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sectsty.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX2e package to help change the style of any or all of LaTeX's
sectional headers in the article, book, or report classes. Examples
include the addition of rules above or below a section title.

