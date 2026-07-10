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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides functionality to cite BibTeX entries with QR codes
for easy sharing and referencing. The target of the QR code is the
entry's digital object identifier (DOI), or URL if no DOI exists. It is
realised via the LaTeX packages biblatex and qrcode.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bib2qr
%dir %{_datadir}/texmf-dist/source/latex/bib2qr
%dir %{_datadir}/texmf-dist/tex/latex/bib2qr
%doc %{_datadir}/texmf-dist/doc/latex/bib2qr/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bib2qr/bib2qr.pdf
%doc %{_datadir}/texmf-dist/source/latex/bib2qr/bib2qr.dtx
%doc %{_datadir}/texmf-dist/source/latex/bib2qr/bib2qr.ins
%{_datadir}/texmf-dist/tex/latex/bib2qr/bib2qr.sty
