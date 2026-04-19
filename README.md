# copy-files

<p>
  <img alt="Python" src="https://img.shields.io/badge/python-3.7%2B-blue?logo=python&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
  <img alt="Status" src="https://img.shields.io/badge/status-stable-green">
</p>

> Herramienta Python para copiar archivos en lote a partir de una lista `.txt`. GUI Tkinter + backend scripteable. **Cero dependencias externas** — solo stdlib.

## Features

- Copia archivos listados en un `.txt` a un destino configurable, respetando (o aplanando) la estructura.
- GUI Tkinter (`UI.py`) o uso directo del backend desde CLI / como módulo Python.
- Utilidad de comparación de listas: dada una lista A y una lista B, exporta los elementos faltantes en cada una.
- Utilidad de prefijo: agrega un path base a cada línea de un archivo de texto.

## Requirements

- Python 3.7+
- **Sin dependencias externas** — no hay que correr `pip install`.

## Quickstart

```bash
git clone https://github.com/GDelpo/copy-files.git
cd copy-files
python UI.py
```

## Componentes

| Archivo | Descripción |
|---------|-------------|
| `UI.py` | Entry point con GUI Tkinter |
| `backend.py` | Lógica de copia — usable desde CLI o como `import` |
| `diff_txt.py` | Compara dos `.txt` y exporta los elementos faltantes |
| `agrega_prefijo.py` | Agrega un prefijo de ruta a cada línea de un `.txt` |

## Usage programática

```python
from backend import copy_from_list

copy_from_list(
    list_file="files_to_copy.txt",
    destination="C:/backup",
    flatten=False,  # True para ignorar estructura de carpetas
)
```

## License

[MIT](LICENSE) © 2026 Guido Delponte
