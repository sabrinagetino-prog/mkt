#!/usr/bin/env python3
"""Build the Fides x Ayres Haus PDF deck."""
from weasyprint import HTML, CSS
from pathlib import Path

OUT = Path(__file__).parent / "fides-ayres-deck.pdf"
HTML_PATH = Path(__file__).parent / "deck.html"

HTML(filename=str(HTML_PATH)).write_pdf(str(OUT))
print(f"PDF generado: {OUT}")
