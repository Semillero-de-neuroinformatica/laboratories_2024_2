
# Entornos Virtuales con Conda

## ¿Qué es un entorno virtual?
Un entorno virtual es un directorio que contiene una instalación independiente de Python y las bibliotecas necesarias para un proyecto específico. Los entornos virtuales permiten aislar las dependencias de un proyecto para evitar conflictos con otros proyectos.

## Ventajas de usar entornos virtuales
- **Aislamiento**: Cada entorno tiene sus propias dependencias y versiones de paquetes, lo que evita conflictos.
- **Reproducibilidad**: Puedes recrear el entorno en diferentes máquinas con las mismas versiones de paquetes.
- **Facilidad de gestión**: Instalar, actualizar y eliminar paquetes dentro de un entorno específico no afecta a otros proyectos.

## ¿Qué es Conda?
`conda` es un sistema de gestión de paquetes y entornos que permite crear y administrar entornos virtuales no solo para Python, sino también para otros lenguajes como R.

## Instalación de Conda
Conda se incluye con Anaconda y Miniconda. Puedes instalar Miniconda siguiendo las instrucciones en [Miniconda Installation](https://docs.conda.io/en/latest/miniconda.html).

## Creación de un entorno virtual con Conda
Para crear un entorno virtual en `conda`, usa el siguiente comando:

```bash
conda create --name nombre_del_entorno
```

Por ejemplo:

```bash
conda create --name mi_entorno
```

## Activación y desactivación de un entorno
Para activar el entorno, utiliza el comando:

```bash
conda activate nombre_del_entorno
```

Por ejemplo:

```bash
conda activate mi_entorno
```

Para desactivar el entorno actual, simplemente usa:

```bash
conda deactivate
```

## Instalación de paquetes en un entorno
Puedes instalar paquetes específicos en un entorno activo utilizando el comando `conda install`:

```bash
conda install nombre_paquete
```

Por ejemplo, para instalar NumPy:

```bash
conda install numpy
```

## Listar todos los entornos
Para ver una lista de todos los entornos creados, utiliza:

```bash
conda info --envs
```

## Eliminación de un entorno
Para eliminar un entorno, asegúrate de que esté desactivado y luego usa:

```bash
conda remove --name nombre_del_entorno --all
```

## Exportar y reproducir un entorno
Para compartir o recrear un entorno en otra máquina, puedes exportar la lista de dependencias a un archivo YAML:

```bash
conda env export --name nombre_del_entorno > entorno.yml
```

Y luego, en la otra máquina, puedes recrear el entorno usando:

```bash
conda env create --file entorno.yml
```

