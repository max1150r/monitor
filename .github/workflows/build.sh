#!/usr/bin/env sh
set -eu

python3 -m pip install -r requirements-build.txt
python3 -m PyInstaller --noconfirm --clean StockWatch.spec
printf '\nEjecutable generado en: dist/StockWatch\n'
