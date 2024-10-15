import sys
from clases import Read_CSV, Read_Mat  # Asegúrate de que las clases estén en el archivo 'clases.py'

archivos_csv = [
    r'C:\Users\VICTUS\Desktop\UdeA\Cuarto Semestre\Informática 2\P2 repository\Parcial2_info2\cancer patient data sets.csv',
    r'C:\Users\VICTUS\Desktop\UdeA\Cuarto Semestre\Informática 2\P2 repository\Parcial2_info2\MMSE 1.csv'
]

archivos_mat = [
    r'C:\Users\VICTUS\Desktop\UdeA\Cuarto Semestre\Informática 2\P2 repository\Parcial2_info2\S1.mat',
    r'C:\Users\VICTUS\Desktop\UdeA\Cuarto Semestre\Informática 2\P2 repository\Parcial2_info2\S2.mat'
]

def mostrar_opciones(archivos, tipo_archivo):
    print(f"\nSeleccione un {tipo_archivo} de la lista:")
    for idx, archivo in enumerate(archivos, start=1):
        print(f"{idx}. {archivo}")
    while True:
        opcion = input(f"Ingrese el número del {tipo_archivo} que desea cargar: ")
        try:
            opcion = int(opcion) - 1
            if 0 <= opcion < len(archivos):
                return archivos[opcion]
            else:
                raise ValueError
        except ValueError:
            print("Opción inválida, por favor ingrese un número válido.")

def menu_principal():
    menu = """
    MENÚ PRINCIPAL
    1. Cargar archivo CSV
    2. Cargar archivo MAT
    3. Graficar gráfico de barras (CSV)
    4. Graficar gráfico de dispersión (CSV)
    5. Mostrar matrices disponibles (MAT)
    6. Graficar datos de una matriz (MAT)
    7. Graficar datos de una matriz con ruido (MAT)
    8. Salir
    """
    lector_csv = None
    lector_mat = None

    while True:
        print(menu)
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                ruta_csv = mostrar_opciones(archivos_csv, "archivo CSV")
                lector_csv = Read_CSV(ruta_csv)
                lector_csv.load_csv()

            elif opcion == "2":
                ruta_mat = mostrar_opciones(archivos_mat, "archivo MAT")
                lector_mat = Read_Mat(ruta_mat)
                lector_mat.load_mat()

            elif opcion == "3":
                if lector_csv is not None:
                    lector_csv.graficar_barras()
                else:
                    raise ValueError("Primero debe cargar un archivo CSV.")

            elif opcion == "4":
                if lector_csv is not None:
                    lector_csv.graficar_dispersion()
                else:
                    raise ValueError("Primero debe cargar un archivo CSV.")

            elif opcion == "5":
                if lector_mat is not None:
                    lector_mat.display_matrices()
                else:
                    raise ValueError("Primero debe cargar un archivo MAT.")

            elif opcion == "6":
                if lector_mat is not None:
                    lector_mat.graficar_todos()
                else:
                    raise ValueError("Primero debe cargar un archivo MAT.")

            elif opcion == "7":
                if lector_mat is not None:
                    lector_mat.graficar_ruido()
                else:
                    raise ValueError("Primero debe cargar un archivo MAT.")

            elif opcion == "8":
                print("Saliendo del programa...")
                sys.exit()

            else:
                raise ValueError("Opción no válida, intente nuevamente.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except FileNotFoundError as fnf_error:
            print(f"Error: {fnf_error}")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    menu_principal()