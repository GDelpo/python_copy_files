# File Batch Copier

## Repositorio

```bash
git clone http://192.168.190.95/forgejo/noble/copy-files.git
git pull origin main   # actualizar
```

> Primera vez en una máquina nueva: ver [SETUP.md](http://192.168.190.95/forgejo/noble/workspace/raw/branch/main/SETUP.md) para configurar proxy y credenciales Git.

---


Herramienta Python para **copiar archivos en lote** a partir de una lista en `.txt`. Incluye interfaz gráfica, backend scripteable y utilidades de apoyo.

No requiere dependencias externas — solo biblioteca estándar de Python.

---

## Herramientas incluidas

| Archivo | Descripción |
|---------|-------------|
| `UI.py` | Interfaz gráfica (tkinter) — punto de entrada principal |
| `backend.py` | Lógica central, usable desde CLI o como módulo |
| `diff_txt.py` | Compara dos listas y exporta los elementos faltantes |
| `agrega_prefijo.py` | Agrega un prefijo de ruta a cada línea de un archivo |

---

## Requisitos

- Python 3.7+
- Sin dependencias externas (`pip install` no necesario)

---

## Uso

### Interfaz gráfica

```bash
python UI.py
```

1. **Listado (.txt):** seleccioná el `.txt` con las rutas completas de los archivos a copiar (una por línea).
2. **Destino:** seleccioná la carpeta de destino.
3. Hacé clic en **PROCESAR LOTE**.

El progreso se muestra en tiempo real. Si hubo errores, se genera automáticamente un reporte `errores_YYYYMMDD_HHMMSS.txt` en la carpeta destino.

---

### Backend por línea de comandos

```bash
python backend.py <lista.txt> <destino/>
```

El `.txt` debe tener una ruta absoluta por línea:

```
C:/documentos/informe.pdf
C:/imagenes/foto.jpg
/home/usuario/datos/archivo.csv
```

---

### Encontrar archivos faltantes entre dos listas

```bash
python diff_txt.py --total lista_completa.txt --actual lista_actual.txt --salida faltantes.txt
```

| Argumento | Descripción |
|-----------|-------------|
| `--total` | Lista completa esperada |
| `--actual` | Lista de lo que existe actualmente |
| `--salida` | Archivo de salida (default: `faltantes.txt`) |

---

### Agregar prefijo de ruta a una lista

Útil para convertir nombres de archivo sueltos en rutas completas antes de pasarlos al copiador.

```bash
python agrega_prefijo.py --prefijo "\\servidor\carpeta\" --entrada nombres.txt --salida rutas.txt
python agrega_prefijo.py --prefijo "/mnt/nas/datos/" --entrada nombres.txt --salida rutas.txt
```

| Argumento | Descripción |
|-----------|-------------|
| `--prefijo` | Prefijo a agregar (ruta local, de red, etc.) |
| `--entrada` | Archivo de entrada (default: `lista.txt`) |
| `--salida` | Archivo de salida (default: `lista_prefijada.txt`) |

---

## Flujo típico de uso

```
lista_completa.txt  ──►  diff_txt.py  ──►  faltantes.txt
                                                │
                                    agrega_prefijo.py  ──►  rutas_completas.txt
                                                                    │
                                                           UI.py / backend.py  ──►  destino/
```

---

## Licencia

MIT
