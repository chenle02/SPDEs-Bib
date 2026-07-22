# SPDEs-Bib GitHub recovery-mirror gate: Ben Arous--Bourgade--McKenna landscape

- Date: 2026-07-22
- Citekey: `ben-arous.bourgade.ea:24:landscape`
- Public source: arXiv:2105.05051 and DOI 10.1002/cpa.22146
- GitHub recovery-mirror URL: <https://chenle02.github.io/SPDEs-Bib/bib_entries/ben-arous.bourgade.ea:24:landscape.html>
- Scope: one reviewed bibliography record and one bounded missing public HTML leaf

This gate used public bibliographic and paper sources only.

## Source publication

The authoritative refdb record was already pushed at
`395a7bbcb28d3a2dc0fc942963386db28417d884`. The reviewed SPDEs-Bib source
delta was pushed to `main` as
`df60187832e54ea4c3f262e556a145b11b5aaac0` with exactly six paths:

- `All.bib`
- `Build_docs/By-Cite-Keys.rst`
- `Build_docs/bib_entries/ben-arous.bourgade.ea:24:landscape.rst`
- `Build_docs/bib_files/ben-arous.bourgade.ea:24:landscape.bib`
- `Statistics.eps`
- `Statistics.png`

The four generated-source counts agreed at 8,679: `All.bib` records, RST index
entries, `bib_entries/*.rst`, and `bib_files/*.bib`. UTF-8, unique-key, exact
metadata, source-to-generated key-set, and orphan checks passed. At the frozen
source commit, authoritative refdb had 8,681 records: the only source records not
included in this one-record publication were the unrelated concurrent keys
`chen.pu:26:two-time` and `liang:25:parabolic`; SPDEs-Bib had no key absent from
refdb.

`All_Numbered.pdf` was not copied. Its SHA-256 was
`b7f8f94f43c4f02dee54a3dae64c1f4f14f1e78d3fb593e1d0bcf819afa92d23`,
and neither the target citekey nor the distinctive paper title occurred in its
extracted text. The numbered aggregate therefore remains an explicit maintenance
gate rather than being represented as current.

## Ordinary deployment attempt

Source push workflow run
[29941206255](https://github.com/chenle02/SPDEs-Bib/actions/runs/29941206255)
was bound to source commit `df60187832e54ea4c3f262e556a145b11b5aaac0`.
It remained entirely in `actions/checkout@v4` from 2026-07-22 17:10:27 UTC
through 17:15:03 UTC with no later generation or deployment step beginning. This
repeated the retained 46--50 minute large-checkout failure pattern, so the run was
cancelled and preserved rather than deleted or rewritten. Its metadata and log are
under `raw/failed-run-29941206255.*`.

## Frozen public-state audit

The complete recursive public tree was fetched with `truncated: false` before any
public write.

- Base `gh-pages` commit: `af43de0556e61515f268e6cf1cc6430c9d2b8e7b`
- Base tree: `a2961a778771d4ae0519b13e0ae3349fc046d0f3`
- Base blobs: 7,723
- Base HTML files: 7,672
- Base bibliography HTML files: 7,666
- Base WAV files: 28
- Complete base blob-map SHA-256:
  `4b923271cd06df4cfdb3803a1d942d4d76c203310100b978e30a5ab953fe2fc1`
- Complete base WAV-map SHA-256:
  `197c558e0a88828c11d25bcc55e81baca75e3bf6bd62ddc7d7d46323454a9345`

The source checkout had 8,679 bibliography RST pages and 126 uniquely referenced
WAV names. Relative to the public base, 1,021 source record pages and 98 source WAV
references were missing, while eight public record pages were absent from the
source checkout and there were no public-only WAVs. This set disagreement rejected
a sparse broad rebuild with `keep_files`; it justified only the exact missing leaf
named in this gate.

## Reviewed render

The target was rendered with the previously deployed-compatible pinned toolchain:

- Sphinx 7.2.6
- sphinx-press-theme 0.8.0
- sphinxcontrib-bibtex 2.6.5
- Pygments 2.17.2
- bibtexparser 1.4.1

The target HTML contained the citekey, title, all three authors, DOI, arXiv ID,
journal metadata, and the public arXiv link. A leaf-only dependency check found two
pre-existing template defects in the raw render: a stylesheet URL with trailing
whitespace and a navigation link to the absent `Audio_Recent.html`. The retained
patch trims the stylesheet URL and removes only that absent navigation item. After
that bounded hardening, every local `href` and `src` resolved to the frozen public
tree or the approved target addition. The reviewed target SHA-256 was
`cad5f9b9a07785abf75382f8263892b77e7d7087d3cf03f602b51b7f3e4a6717`.

## Bounded non-force public commit

Only the approved path
`bib_entries/ben-arous.bourgade.ea:24:landscape.html` was added.

- New blob: `6f85a916f370552adf1c0bce3fbe8cff1bed6d3e`
- Candidate tree: `971a07dab7c43714a083dbf8660a2e1bd91fecd5`
- Public commit: `cefc016c60b084ff1454075feca26e857ffff064`
- Sole parent: `af43de0556e61515f268e6cf1cc6430c9d2b8e7b`
- Ref update: `force: false`, after an exact live-ref race check
- Candidate blobs: 7,724
- Candidate bibliography HTML files: 7,667
- Candidate complete blob-map SHA-256:
  `17534d4a367f988f9eda404ecfa8fead6848836a0a0e06c9e766bc3de4ab0c65`
- Candidate WAV files: 28
- Candidate WAV-map SHA-256:
  `197c558e0a88828c11d25bcc55e81baca75e3bf6bd62ddc7d7d46323454a9345`

The candidate recursive tree was also complete (`truncated: false`). It proved no
old path disappeared, every old blob SHA was unchanged, the approved HTML leaf was
the only addition, and the complete WAV map was byte-identical.

## GitHub Pages mirror and HTTP receipt

GitHub Pages build
[1109309242](https://api.github.com/repos/chenle02/SPDEs-Bib/pages/builds/1109309242)
built the exact public commit `cefc016c60b084ff1454075feca26e857ffff064`.
It ran from 2026-07-22 17:16:14 UTC through 17:18:59 UTC and finished with status
`built` and no error.

The exact target URL returned HTTP 200. Its served SHA-256 was
`cad5f9b9a07785abf75382f8263892b77e7d7087d3cf03f602b51b7f3e4a6717`,
byte-identical to the reviewed target. The served body contained the citekey,
paper title, Ben Arous, Bourgade, McKenna, DOI `10.1002/cpa.22146`, and arXiv
identifier `2105.05051`.

Two old public sentinels remained HTTP 200 and byte-identical before and after the
update:

- Aaronson HTML:
  <https://chenle02.github.io/SPDEs-Bib/bib_entries/aaronson:97:introduction.html>,
  SHA-256 `5e2e6d5a6c67682b0ef38e83b489631a2d92227b825ffcc88a764fea37e0b155`
- Alberts audio:
  <https://chenle02.github.io/SPDEs-Bib/alberts_khanin_ea-14-continuum.wav>,
  SHA-256 `b4c8473c3d94ba120c4723d806189b0b36997bc05e949baf08c33bbcfa18820b`

## Recovery and collateral-diff notes

No interactive prompt loop was used in this publication stage. The broad
`publish.sh` was deliberately not invoked because it would have copied the known
stale numbered PDF.

During isolated generation, `licence.sh` was first invoked from `Build_docs/`
instead of the repository root. It created an untracked header-only
`Build_docs/All.bib`; that scratch file was deleted immediately, the command was
rerun from the correct root, and no canonical or committed artifact was affected.
`Bibtexparser-all.py --fast` also rewrote 126 podcast-injected RST pages because
the sparse clone intentionally omitted the multi-gigabyte audio directory. All
126 collateral changes were restored from the frozen base, as was the Sphinx-side
`Audio_Recent.rst` rewrite. The final staged source allowlist was exactly the six
paths listed above.

## Explicit boundary and open gates

This receipt proves the named leaf page is resolvable on the GitHub recovery
mirror and preserves the entire prior mirror tree. It does not complete the
primary Read the Docs publication gate and is not a broad site reconciliation:

- global source/public record parity remains 8,679 versus 7,667 after the overlay;
- `By-Cite-Keys.html`, other generated indexes, and search remain stale for this
  leaf overlay;
- source/public audio-reference parity remains 126 versus 28;
- `All_Numbered.pdf` remains stale;
- the two unrelated concurrent refdb records named above require their own source
  publication.
- the exact primary Read the Docs record page must return HTTP 200 before this
  record can be called publicly published or used to approve `audited: true`.

The raw directory retains the source counts and hashes, complete base and candidate
Git trees, normalized maps and digests, parity lists, pinned toolchain, render and
workflow logs, exact Git API payloads/responses, Pages build object, served target,
HTTP/hash TSVs, and pre/post sentinel hashes. The large WAV sentinel bodies and
Sphinx doctree caches were intentionally not committed; their byte hashes and live
HTTP receipts are retained.
