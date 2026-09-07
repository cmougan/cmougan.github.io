from pathlib import Path
import shutil
import subprocess
import zipfile


# ============================================================
# PATHS
# ============================================================

ROOT = Path(__file__).resolve().parent

INDEX = ROOT / "index.md"
SECTIONS = ROOT / "sections"
BIBLIOGRAPHY = ROOT / "references.bib"
CSS = ROOT / "styles.css"
TEMPLATE = ROOT / "template.html"

HTML = ROOT / "index.html"
PDF = ROOT / "paper.pdf"
TEX = ROOT / "paper.tex"
ARXIV_ZIP = ROOT / "arxiv-source.zip"


# ============================================================
# CHECK DEPENDENCIES
# ============================================================

for command in ["pandoc", "tectonic"]:
    if shutil.which(command) is None:
        raise SystemExit(
            f"{command} is not installed.\n"
            f"Install it with:\n\n"
            f"    brew install {command}\n"
        )


# ============================================================
# SOURCES
# ============================================================

sources = [
    INDEX,
    *sorted(SECTIONS.glob("*.md")),
]

source_args = [str(path) for path in sources]


# ============================================================
# HTML
# ============================================================

print("Building HTML...")

html_command = [
    "pandoc",
    *source_args,
    "--standalone",
    "--toc",
    "--number-sections",
    "--citeproc",
    f"--bibliography={BIBLIOGRAPHY}",
    f"--css={CSS.name}",
]

if TEMPLATE.exists():
    html_command.append(f"--template={TEMPLATE}")

html_command += ["-o", str(HTML)]

subprocess.run(
    html_command,
    cwd=ROOT,
    check=True,
)


# ============================================================
# PDF
# ============================================================

print("Building PDF...")

subprocess.run(
    [
        "pandoc",
        *source_args,
        "--standalone",
        "--toc",
        "--number-sections",
        "--citeproc",
        f"--bibliography={BIBLIOGRAPHY}",
        "--pdf-engine=tectonic",
        "-o",
        str(PDF),
    ],
    cwd=ROOT,
    check=True,
)


# ============================================================
# LATEX
# ============================================================

print("Building LaTeX...")

subprocess.run(
    [
        "pandoc",
        *source_args,
        "--standalone",
        "--number-sections",
        "--citeproc",
        f"--bibliography={BIBLIOGRAPHY}",
        "-o",
        str(TEX),
    ],
    cwd=ROOT,
    check=True,
)


# ============================================================
# ARXIV ZIP
# ============================================================

print("Building arXiv package...")

with zipfile.ZipFile(
    ARXIV_ZIP,
    "w",
    compression=zipfile.ZIP_DEFLATED,
) as zip_file:

    zip_file.write(
        TEX,
        arcname="paper.tex",
    )

    if BIBLIOGRAPHY.exists():
        zip_file.write(
            BIBLIOGRAPHY,
            arcname="references.bib",
        )

    figures = ROOT / "figures"

    if figures.exists():
        for file in figures.rglob("*"):
            if file.is_file():
                zip_file.write(
                    file,
                    arcname=file.relative_to(ROOT),
                )


print()
print("Done:")
print(f"  HTML:  {HTML.relative_to(ROOT)}")
print(f"  PDF:   {PDF.relative_to(ROOT)}")
print(f"  LaTeX: {TEX.relative_to(ROOT)}")
print(f"  arXiv: {ARXIV_ZIP.relative_to(ROOT)}")