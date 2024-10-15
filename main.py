import sys
from clases import Read_CSV, Read_Mat  # Asegúrate de que las clases estén en el archivo 'clases.py'

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Cargar archivo CSV")
        print("2. Cargar archivo MAT")
        print("3. Graficar gráfico de barras (CSV)")
        print("4. Graficar gráfico de dispersión (CSV)")
        print("5. Mostrar matrices disponibles (MAT)")
        print("6. Graficar datos de una matriz (MAT)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta_csv = input("Ingrese la ruta del archivo CSV: ")
            lector_csv = Read_CSV(ruta_csv)
            lector_csv.load_csv()
        elif opcion == "2":
            ruta_mat = input("Ingrese la ruta del archivo MAT: ")
            lector_mat = Read_Mat(ruta_mat)
            lector_mat.load_mat()
        elif opcion == "3":
            if 'lector_csv' in locals():
                lector_csv.graficar_barras()
            else:
                print("Primero debe cargar un archivo CSV.")
        elif opcion == "4":
            if 'lector_csv' in locals():
                lector_csv.graficar_dispersion()
            else:
                print("Primero debe cargar un archivo CSV.")
        elif opcion == "5":
            if 'lector_mat' in locals():
                lector_mat.display_matrices()
            else:
                print("Primero debe cargar un archivo MAT.")
        elif opcion == "6":
            if 'lector_mat' in locals():
                lector_mat.graficar_todos()
            else:
                print("Primero debe cargar un archivo MAT.")
        elif opcion == "7":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()