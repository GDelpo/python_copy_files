# diff_txt.py
# Compara dos archivos de texto (uno por línea) y guarda las líneas
# que están en el primero pero no en el segundo (los "faltantes").
#
# Uso:
#   python diff_txt.py --total lista_total.txt --actual lista_actual.txt --salida faltantes.txt

import argparse

def encontrar_faltantes(total: str, actual: str, salida: str):
    with open(total, 'r', encoding='utf-8') as f:
        set_total = set(line.strip() for line in f if line.strip())

    with open(actual, 'r', encoding='utf-8') as f:
        set_actual = set(line.strip() for line in f if line.strip())

    faltantes = sorted(set_total - set_actual)

    with open(salida, 'w', encoding='utf-8') as f_out:
        for item in faltantes:
            f_out.write(item + '\n')

    print(f"{len(faltantes)} elementos faltantes guardados en: {salida}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encuentra elementos presentes en la lista total pero ausentes en la lista actual."
    )
    parser.add_argument('--total', required=True, help='Archivo con la lista completa esperada')
    parser.add_argument('--actual', required=True, help='Archivo con la lista de lo que existe actualmente')
    parser.add_argument('--salida', default='faltantes.txt', help='Archivo de salida (default: faltantes.txt)')
    args = parser.parse_args()

    encontrar_faltantes(args.total, args.actual, args.salida)