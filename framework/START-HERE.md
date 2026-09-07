# Add a Markdown + Pandoc paper to cmougan.eu

The document will live at:

https://www.cmougan.eu/papers/my-paper/

The paper is plain Markdown and Pandoc.

## What you edit

```text
papers/my-paper/
├── index.md                       # title, authors, abstract
├── sections/
│   ├── 01-introduction.md
│   ├── 02-main-argument.md
│   ├── 03-evidence-and-method.md
│   ├── 04-discussion.md
│   └── 05-conclusion.md
├── references.bib                 # bibliography
├── figures/                       # figures
├── styles.css                     # webpage styling
├── template.html                  # webpage shell
└── build.py                       # Pandoc build
```

`build.py` gives Pandoc `index.md` followed by every Markdown file in
`sections/`, sorted by filename. Pandoc treats them as one document.

To change the order, rename the section files. To add a section, for example:

```text
sections/03-related-work.md
```

The numbering in the filename controls its position; the filename itself is
not shown in the paper.

## Upload once

Extract this ZIP into the root of your existing `cmougan.github.io` repository,
including the hidden `.github` folder. It does not replace your existing root
`index.html`, `CNAME`, images, CSS, or moving object.

In GitHub, open **Settings → Pages → Build and deployment → Source** and select
**GitHub Actions**. Keep your existing custom domain unchanged.

Then from the repository root:

```bash
git add START-HERE.md papers/my-paper .github/workflows/publish-paper.yml
git commit -m "Add Markdown paper"
git push origin master
```

The workflow builds the paper and publishes it alongside the existing site.

To link to it from your homepage:

```html
<a href="/papers/my-paper/">Research paper</a>
```

## Everyday writing

Most of the time, just edit one of the files in `sections/` and push:

```bash
git add papers/my-paper
git commit -m "Update paper"
git push origin master
```

The build produces:

```text
index.html          webpage
paper.pdf           paper PDF
paper.tex           generated LaTeX
arxiv-source.zip    LaTeX source package for arXiv
```

References go in `references.bib` and can be cited from any section as:

```markdown
This has been discussed previously [@reference-key].
```

## Contributions

The webpage's **Suggest an edit** link opens the `sections/` folder on GitHub.
A contributor chooses the relevant Markdown file, uses GitHub's browser editor,
and proposes a pull request. They do not need Pandoc or LaTeX locally.

## Optional local build

On macOS with Homebrew:

```bash
brew install pandoc
brew install --cask mactex-no-gui
```

Then build from anywhere inside your repository with:

```bash
python3 papers/my-paper/build.py
```

For a lightweight local HTML preview without producing the PDF:

```bash
cd papers/my-paper
pandoc index.md sections/*.md \
  --standalone --citeproc --bibliography=references.bib \
  --toc --number-sections --mathml \
  --template=template.html --css=styles.css --embed-resources \
  -V home-url:/ \
  -V edit-url:https://github.com/cmougan/cmougan.github.io/tree/master/papers/my-paper/sections \
  -V history-url:https://github.com/cmougan/cmougan.github.io/commits/master/papers/my-paper \
  -V pdf-url:paper.pdf \
  -V arxiv-source-url:arxiv-source.zip \
  -o index.html
```

For normal use, `python3 papers/my-paper/build.py` is simpler.

## arXiv

Use `arxiv-source.zip`. It contains the generated `paper.tex` and local figure
files needed by the paper. Always inspect the PDF compiled by arXiv before
submitting.
