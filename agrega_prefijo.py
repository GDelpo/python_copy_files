# agrega_prefijo.py
# Agrega un prefijo a cada línea de un archivo de texto.
#
# Uso:
#   python agrega_prefijo.py --prefijo "\\servidor\carpeta\" --entrada faltantes.txt --salida faltantes_prefijados.txt
#   python agrega_prefijo.py --prefijo "/mnt/nas/archivos/" --entrada lista.txt

import argparse

def agregar_prefijo(prefijo: str, entrada: str, salida: str):
    with open(entrada, 'r', encoding='utf-8') as fin, open(salida, 'w', encoding='utf-8') as fout:
        for linea in fin:
            linea = linea.strip()
            if linea:
                fout.write(f'{prefijo}{linea}\n')
    print(f'Archivo generado: {salida}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Agrega un prefijo de ruta a cada línea de un archivo de texto."
    )
    parser.add_argument('--prefijo', required=True, help='Prefijo a agregar (ej: "C:\\Archivos\\" o "/mnt/nas/")')
    parser.add_argument('--entrada', default='lista.txt', help='Archivo de entrada (default: lista.txt)')
    parser.add_argument('--salida', default='lista_prefijada.txt', help='Archivo de salida (default: lista_prefijada.txt)')
    args = parser.parse_args()

    agregar_prefijo(args.prefijo, args.entrada, args.salida)
