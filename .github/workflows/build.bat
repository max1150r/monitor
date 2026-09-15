@echo off
setlocal
py -m pip install -r requirements-build.txt || exit /b 1
py -m PyInstaller --noconfirm --clean StockWatch.spec || exit /b 1
echo.
echo Ejecutable generado en: dist\StockWatch.exe
