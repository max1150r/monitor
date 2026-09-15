diff --git a/README.md b/README.md
index 2578eff9e962670785787ec24090ee6e83151abe..51838a9c463f485d921d14ee0125cbbbd3d896b8 100644
--- a/README.md
+++ b/README.md
@@ -1,18 +1,77 @@
-H5P Drag Question
-==========
+StockWatch Carrefour
+====================
+
+Aplicación web local para consultar si un producto de Carrefour está disponible o
+agotado. Analiza primero los datos estructurados `Product`/`Offer` publicados por
+la tienda y usa señales visibles de la página como respaldo. No compra productos
+ni elude mecanismos de acceso del comercio.
+
+## Uso
+
+Requiere Python 3.10 o posterior y no necesita instalar dependencias:
+
+```bash
+python3 server.py
+```
+
+Abre `http://localhost:8080`, pega la URL HTTPS del producto y pulsa **Comprobar
+stock**. Mientras la pestaña permanezca abierta, se repite la comprobación cada
+cinco minutos; también puede actualizarse manualmente. Este intervalo moderado
+evita generar tráfico abusivo.
+
+## Crear un ejecutable
+
+Si solo quieres descargar todos los archivos juntos, utiliza
+[`downloads/StockWatch-codigo-fuente.zip`](downloads/StockWatch-codigo-fuente.zip),
+descomprímelo y sigue las instrucciones siguientes.
+
+El ejecutable incluye Python y todos los archivos de la interfaz, por lo que la
+persona que lo use no necesita instalar Python. Debe compilarse en el mismo
+sistema operativo donde se vaya a utilizar (Windows para generar `.exe`, Linux
+para generar un binario Linux).
+
+En **Windows**, abre una consola en la carpeta del proyecto y ejecuta:
+
+```bat
+build.bat
+```
+
+En **Linux o macOS**:
+
+```bash
+./build.sh
+```
+
+El resultado queda en `dist/StockWatch` (`dist\StockWatch.exe` en Windows). Al
+abrirlo, StockWatch inicia el servidor y abre automáticamente el navegador. Se
+puede elegir otro puerto con `StockWatch --port 9090` o evitar que abra el
+navegador con `StockWatch --no-browser`.
+
+También se incluye el flujo **Compilar ejecutables** de GitHub Actions. Puede
+ejecutarse manualmente desde la pestaña *Actions* y produce artefactos listos
+para descargar para Windows, Linux y macOS. Al crear una etiqueta que comience
+por `v` (por ejemplo, `v1.0.0`) el flujo se ejecuta automáticamente.
+
+```bash
+python3 -m unittest discover -s tests -v
+```
+
+## Proyecto original
+
+Este repositorio partió de H5P Drag Question.
 
 Drag and drop the elements into the correct drop zones.
 Test your users with drag and drop tasks.
 Can be used in Question Sets, Course Presentations and Interactive Videos.
 
 ## License
 
 (The MIT License)
 
 Copyright (c) 2012-2014 Amendor AS
  
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
  
 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
  
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
