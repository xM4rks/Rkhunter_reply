import hashlib
import os

DIRECTORIOS_SISTEMA = [
    "/bin",
]

LOG_HASHES = "negatives_logs.txt"
LOG_ERRORES = "errors_logs.txt"


def inicializar_programa():
    ##Prepara los hashes y limpia los archivos de log.
    hashes = {}

    open(LOG_HASHES, "w").close()
    open(LOG_ERRORES, "w").close()

    return hashes


def analizar_archivos(hashes):
    ##Analiza los archivos y guarda los resultados en los logs.
    for directorio in DIRECTORIOS_SISTEMA:
        for ruta, carpetas, ficheros in os.walk(directorio):
            for fichero in ficheros:
                archivo = os.path.join(ruta, fichero)

                try:
                    with open(archivo, "rb") as fichero_binario:
                        hash_sha256 = hashlib.sha256(
                            fichero_binario.read()
                        ).hexdigest()

                    if archivo in hashes and hash_sha256 == hashes[archivo]:
                        print(f"[OK] {archivo}")
                    else:
                        print(f"[WARNING] {archivo}")
                        with open(LOG_HASHES, "a") as log:
                            log.write(
                                f"{archivo} - HASH: {hash_sha256}\n"
                            )

                except (PermissionError, OSError) as error:
                    print(f"Warning: {archivo}: {error}")
                    with open(LOG_ERRORES, "a") as log:
                        log.write(f"{archivo} - ERROR: {error}\n")


def main():
    hashes = inicializar_programa()
    analizar_archivos(hashes)


if __name__ == "__main__":
    main()
