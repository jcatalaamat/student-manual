#!/bin/bash

# Being Human 101 V2 - Convert to PREMIUM PDF
# This script converts the markdown manual to a beautifully formatted PDF

INPUT_FILE="Being Human 101 - Student Manual V2.md"
OUTPUT_FILE="Being-Human-101-Student-Manual-V2-PREMIUM.pdf"

echo "Converting Being Human 101 V2 Manual to PREMIUM PDF..."

# Premium conversion with custom styling
pandoc "$INPUT_FILE" \
  -o "$OUTPUT_FILE" \
  --pdf-engine=xelatex \
  -V geometry:margin=1.25in \
  -V fontsize=11pt \
  -V documentclass=book \
  -V classoption=openany \
  -V papersize=letter \
  -V mainfont="Helvetica" \
  -V monofont="Courier" \
  --toc \
  --toc-depth=3 \
  -V toc-title="Table of Contents" \
  -V colorlinks=true \
  -V linkcolor=NavyBlue \
  -V urlcolor=NavyBlue \
  -V toccolor=black \
  --highlight-style=tango \
  -V linestretch=1.2 \
  --number-sections \
  -V header-includes='\usepackage{fancyhdr} \pagestyle{fancy} \fancyhead[L]{Being Human 101} \fancyhead[R]{Student Manual V2} \fancyfoot[C]{\thepage}'

echo "✅ PREMIUM PDF created: $OUTPUT_FILE"
echo ""
echo "File location: $(pwd)/$OUTPUT_FILE"
echo ""
echo "Features:"
echo "  ✅ Professional book layout"
echo "  ✅ Table of contents (3 levels deep)"
echo "  ✅ Custom headers and footers"
echo "  ✅ Numbered sections"
echo "  ✅ Clickable links"
echo "  ✅ 1.25 inch margins"
