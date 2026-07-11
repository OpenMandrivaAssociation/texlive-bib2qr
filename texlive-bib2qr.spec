%global tl_name bib2qr
%global tl_revision 71940

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Cite BibTeX entries with QR codes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bib2qr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2qr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2qr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2qr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides functionality to cite BibTeX entries with QR codes
for easy sharing and referencing. The target of the QR code is the
entry's digital object identifier (DOI), or URL if no DOI exists. It is
realised via the LaTeX packages biblatex and qrcode.

