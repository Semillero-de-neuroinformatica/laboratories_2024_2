
### **Cuaderno de Entrenamiento en Gestión de Archivos**
Este cuaderno cubre los comandos básicos que necesitarás para gestionar archivos en la terminal\. Aprender estos comandos te ayudará a navegar y manipular archivos y directorios de manera eficiente\.
### **Listando Archivos y Directorios**
* **Listar todos los archivos y directorios en el directorio actual\:**
```warp-runnable-command
  ls 
```
  **Ejemplo\:** Listar el contenido del directorio actual\.
* **Listar todos los archivos\, incluidos los archivos ocultos\:**
```warp-runnable-command
  ls -a
```
  **Ejemplo\:** Listar todos los archivos\, incluidos los ocultos\, en el directorio actual\.
* **Listar archivos con información detallada \(permisos\, propiedad\, tamaño y fecha\/hora de modificación\)\:**
```warp-runnable-command
  ls -l
```
  **Ejemplo\:** Listar todos los archivos con información detallada\.
* **Listar archivos con información detallada\, incluidos los archivos ocultos\:**
```warp-runnable-command
  ls -la
```
  **Ejemplo\:** Listar todos los archivos\, incluidos los ocultos\, con información detallada\.
### **Cambiando de Directorio**
* **Cambiar a un directorio específico\:**
```warp-runnable-command
  cd /ruta/al/directorio
```
  **Ejemplo\:** Cambiar al directorio `/usr/local`\.
* **Subir un directorio\:**
```warp-runnable-command
  cd ..
```
  **Ejemplo\:** Si estás en `/usr/local/bin`\, este comando te llevará a `/usr/local`\.
* **Moverse al directorio home\:**
```warp-runnable-command
  cd ~
```
  **Ejemplo\:** Este comando te lleva de regreso a tu directorio home desde cualquier ubicación\.
* **Cambiar al directorio anterior\:**
```warp-runnable-command
  cd - 
```
  **Ejemplo\:** Este comando te lleva de regreso al último directorio en el que estuviste\.
### **Creando Directorios**
* **Crear un nuevo directorio\:**
```warp-runnable-command
  mkdir /ruta/al/nuevo_directorio
```
  **Ejemplo\:** Crear un directorio llamado `proyectos` en el directorio actual\.
### **Moviendo y Renombrando Archivos**
* **Mover o renombrar un archivo\:**
```warp-runnable-command
  mv /ruta/al/origen /ruta/al/destino
```
  **Ejemplo\:** Renombrar un archivo `nombre_viejo.txt` a `nombre_nuevo.txt` en el mismo directorio\:
```warp-runnable-command
  mv nombre_viejo.txt nombre_nuevo.txt
```
  **Ejemplo\:** Mover `archivo.txt` al directorio `Documentos`\:

```warp-runnable-command
  mv archivo.txt ~/Documentos/
```
### **Copiando Archivos**
* **Copiar un archivo\:**
```warp-runnable-command
  cp /ruta/al/origen /ruta/al/destino
  
```
  **Ejemplo\:** Copiar `archivo.txt` al directorio `Documentos`\:
```warp-runnable-command
  cp archivo.txt ~/Documentos/
```
* **Copiar un directorio y su contenido\:**
```warp-runnable-command
  cp -r /ruta/al/directorio_origen /ruta/al/directorio_destino
```
  **Ejemplo\:** Copiar todo el directorio `proyectos` a `proyectos_respaldo`\:
```warp-runnable-command
  cp -r proyectos proyectos_respaldo
```
### **Eliminando Archivos y Directorios**
* **Eliminar un archivo\:**
```warp-runnable-command
  rm /ruta/al/archivo
```
  **Ejemplo\:** Eliminar `innecesario.txt`\:
```warp-runnable-command
  rm innecesario.txt
```
* **Eliminar un directorio vacío\:**
```warp-runnable-command
  rmdir /ruta/al/directorio 
```
  **Ejemplo\:** Eliminar un directorio vacío `proyectos_viejos`\:
```warp-runnable-command
  rmdir proyectos_viejos
```
* **Eliminar un directorio y su contenido\:**
```warp-runnable-command
  rm -r /ruta/al/directorio
```
  **Ejemplo\:** Eliminar el directorio `proyectos_viejos` y todo su contenido\:
```warp-runnable-command
  rm -r proyectos_viejos
```
