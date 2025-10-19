#!/bin/bash

# Being Human 101 V2 - Convert to PDF
# This script converts the markdown manual to a professional PDF

INPUT_FILE="Being Human 101 - Student Manual V2.md"
OUTPUT_FILE="Being-Human-101-Student-Manual-V2.pdf"

echo "Converting Being Human 101 V2 Manual to PDF..."

# Basic conversion (simple, fast)
pandoc "$INPUT_FILE" \
  -o "$OUTPUT_FILE" \
  --pdf-engine=pdflatex \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V documentclass=report \
  --toc \
  --toc-depth=2 \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue

echo "✅ PDF created: $OUTPUT_FILE"
echo ""
echo "File location: $(pwd)/$OUTPUT_FILE"
