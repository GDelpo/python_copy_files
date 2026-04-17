# backend.py
import shutil
from pathlib import Path
from typing import List, Callable, Dict
from datetime import datetime

def leer_listado_desde_txt(ruta_txt: str) -> List[str]:
    ruta = Path(ruta_txt)
    if not ruta.exists():
        return []

    lista_limpia = []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if linea_limpia: 
                lista_limpia.append(linea_limpia)
    return lista_limpia

def copiar_archivo(ruta_origen: str, directorio_destino: Path, logger: Callable) -> str:
    """
    Retorna el estado: 'OK', 'ERROR', 'SKIP'
    """
    origen = Path(ruta_origen)
    
    if not origen.exists():
        logger(f"⚠️  No encontrado: {origen.name}")
        return "ERROR"

    destino_final = directorio_destino / origen.name
    
    if destino_final.exists():
        logger(f"⏭️  Saltado (Ya existe): {origen.name}")
        return "SKIP"

    try:
        shutil.copy2(src=origen, dst=destino_final)
        logger(f"✅ Copiado: {origen.name}")
        return "OK"
    except Exception as e:
        logger(f"❌ Error crítico: {e}")
        return "ERROR"

def procesar_lote(ruta_txt: str, ruta_destino: str, logger: Callable = print) -> Dict[str, int]:
    """
    Función principal que orquesta todo.
    Devuelve un diccionario con las estadísticas finales.
    """
    archivos = leer_listado_desde_txt(ruta_txt)
    stats = {"ok": 0, "skip": 0, "error": 0, "errores_lista": []}

    if not archivos:
        logger("❌ No hay archivos en la lista o no se encontró el txt.")
        return stats

    destino = Path(ruta_destino)
    destino.mkdir(parents=True, exist_ok=True)
    
    logger(f"--- Iniciando proceso de {len(archivos)} archivos ---")
    
    for archivo in archivos:
        resultado = copiar_archivo(archivo, destino, logger)
        
        if resultado == "OK":
            stats["ok"] += 1
        elif resultado == "SKIP":
            stats["skip"] += 1
        elif resultado == "ERROR":
            stats["error"] += 1
            stats["errores_lista"].append(archivo)

    # Generar reporte de errores si es necesario
    if stats["errores_lista"]:
        nombre_log = f"errores_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        ruta_log = destino / nombre_log
        try:
            with open(ruta_log, 'w', encoding='utf-8') as f:
                f.write("\n".join(stats["errores_lista"]))
            logger(f"📝 Reporte de errores guardado en: {nombre_log}")
        except:
            pass
            
    logger("--- Proceso finalizado ---")
    return stats

# Esto permite probar el backend solo, sin la UI
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Copia archivos listados en un .txt hacia un directorio destino.")
    parser.add_argument('lista', help='Ruta al .txt con la lista de archivos a copiar')
    parser.add_argument('destino', help='Directorio destino donde se copiarán los archivos')
    args = parser.parse_args()
    procesar_lote(args.lista, args.destino)