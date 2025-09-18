# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
DESTPATH      = $(BUILDDIR)/html/
GHPAGEDIR     = ../../SPDEs-Bib-Docs/

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile gen-audio html

# Generate recent-audio page
gen-audio:
	@python3 generate_audio_recent.py

# Build HTML after generating audio index
html: gen-audio
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w warnings.log

# Add new deploy target
deploy:
	rsync -av --delete --exclude='.*' "$(DESTPATH)" "$(GHPAGEDIR)"
	# cd "$(GHPAGEDIR)" && git add . && opencommit --yes && git push
	cd "$(GHPAGEDIR)" && git diff-index --quiet HEAD || (git add . && git commit -m "docs: update Sphinx documentation build" && git push)


# New target that combines html and deploy
html-and-deploy: html deploy

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w warnings.log
