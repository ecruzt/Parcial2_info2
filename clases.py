import scipy.io as sio
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Read_CSV:
    """
    Clase para manipular archivos CSV.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.columnas_disponibles = []

    def load_csv(self):
        """
        Carga el archivo CSV en un DataFrame de Pandas y guarda las columnas disponibles.
        """
        try:
            self.data = pd.read_csv(self.file_path, index_col=0)
            self.columnas_disponibles = self.data.columns.tolist()  # Guardar las columnas
            print(f"Archivo {self.file_path} cargado exitosamente.")
        except FileNotFoundError:
            print(f"Error: El archivo {self.file_path} no fue encontrado.")
        except pd.errors.EmptyDataError:
            print("Error: El archivo está vacío.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el archivo: {e}")

    def obtener_columnas(self):
        """
        Devuelve las columnas disponibles.
        """
        if self.data is not None:
            return self.columnas_disponibles
        else:
            print("No se han cargado datos.")
            return []

    def solicitar_columnas(self):
        """
        Solicita al usuario que ingrese las columnas a graficar y las compara con las disponibles.
        """
        if self.data is not None:
            print("Columnas disponibles:", self.columnas_disponibles)
            columna_x = input("Ingrese la columna para el eje X: ")
            columna_y = input("Ingrese la columna para el eje Y: ")
            
            if columna_x in self.columnas_disponibles and columna_y in self.columnas_disponibles:
                return columna_x, columna_y
            else:
                print(f"Error: Las columnas '{columna_x}' o '{columna_y}' no existen en los datos.")
                return None, None
        else:
            print("No se han cargado datos.")
            return None, None

    def graficar_barras(self):
        """
        Genera un gráfico de barras usando Seaborn, solicitando las columnas al usuario.
        """
        columna_x, columna_y = self.solicitar_columnas()
        if columna_x and columna_y:
            plt.figure(figsize=(10, 6))
            sns.barplot(x=self.data[columna_x], y=self.data[columna_y])
            plt.xlabel(columna_x)
            plt.ylabel(columna_y)
            plt.title(f'Gráfico de barras: {columna_y} vs {columna_x}')
            plt.xticks(rotation=45)
            plt.show()

    def graficar_dispersion(self):
        """
        Genera un gráfico de dispersión usando Seaborn, solicitando las columnas al usuario.
        """
        columna_x, columna_y = self.solicitar_columnas()
        if columna_x and columna_y:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=self.data[columna_x], y=self.data[columna_y])
            plt.xlabel(columna_x)
            plt.ylabel(columna_y)
            plt.title(f'Gráfico de dispersión: {columna_y} vs {columna_x}')
            plt.show()

    def nan_counter_and_cleanup(self):
        if self.data is not None:
            # Contar los valores NaN por columna
            nan_counts = self.data.isna().sum()
            print("Valores NaN por columna:")
            print(nan_counts)

            # Verificar si hay algún valor NaN en total
            total_nans = nan_counts.sum()
            if total_nans == 0:
                print("No hay valores NaN en el DataFrame.")
            else:
                print(f"Total de valores NaN en el DataFrame: {total_nans}")

                # Limpiar las filas que contienen valores NaN
                self.data.dropna(inplace=True)
                print("Filas con valores NaN eliminadas.")
        else:
            print("No se han cargado datos.")
            
    def multiplicar_columnas_y_guardar(self, col1, col2, new_file_name):
        print("Columnas disponibles:", self.columnas_disponibles)
        
        if self.data is not None:
            # Verificar que las columnas existan en el DataFrame
            if col1 in self.data.columns and col2 in self.data.columns:
                # Verificar que las columnas sean numéricas
                if pd.api.types.is_numeric_dtype(self.data[col1]) and pd.api.types.is_numeric_dtype(self.data[col2]):
                    # Crear una nueva columna como la multiplicación de col1 y col2
                    self.data['multiplicacion'] = self.data[col1] * self.data[col2]

                    # Asegurarse de que el nuevo archivo tenga la extensión .csv
                    if not new_file_name.endswith('.csv'):
                        new_file_name += '.csv'
                    
                    # Guardar el DataFrame actualizado en un nuevo archivo CSV
                    self.data.to_csv(new_file_name, index=False)
                    print(f"Nuevo archivo CSV creado: {new_file_name}")
                else:
                    print(f"Una o ambas columnas '{col1}' o '{col2}' no son numéricas.")
            else:
                print(f"Una o ambas columnas '{col1}' o '{col2}' no se encuentran en los datos.")
        else:
            print("No se han cargado datos.")



class Read_Mat:
    """
    Clase para manipular archivos MAT.

    Esta clase permite cargar archivos .mat y acceder a las matrices
    que contienen. Proporciona métodos para cargar el archivo y obtener
    los nombres de las matrices disponibles.
    """

    def __init__(self, file_path):
        """
        Inicializa la clase con la ruta del archivo.

        :param file_path: Ruta al archivo .mat que se va a cargar.
        """
        self.file_path = file_path
        self.data = None
        self.matrix_names = []  # Atributo para guardar los nombres de las matrices

    def load_mat(self):
        """
        Carga el archivo MAT en un diccionario de Python.

        Este método intenta cargar el archivo .mat especificado en la
        ruta proporcionada. Si tiene éxito, almacena los datos y los
        nombres de las matrices disponibles.
        """
        try:
            self.data = sio.loadmat(self.file_path)
            print("Archivo cargado correctamente.")
            self.matrix_names = self.get_matrix_names()  # Almacena los nombres de las matrices
        except FileNotFoundError:
            print(f"Archivo '{self.file_path}' no encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def get_matrix_names(self):
        """
        Devuelve una lista con los nombres de las matrices disponibles.

        :return: Lista de nombres de matrices en el archivo .mat.
        """
        if self.data is not None:
            return [key for key in self.data.keys() if isinstance(self.data[key], np.ndarray) and key[0] != '_']
        else:
            print("No se han cargado datos.")
            return []

    def get_matrix(self, name):
        """
        Devuelve una matriz específica por su nombre.

        :param name: Nombre de la matriz que se desea obtener.
        :return: La matriz correspondiente o None si no existe.
        """
        if self.data is not None and name in self.matrix_names:
            return self.data[name]
        else:
            print(f"Matriz '{name}' no encontrada o no se han cargado datos.")
            return None

    def display_matrices(self):
        """
        Muestra los nombres de las matrices disponibles en el archivo cargado.
        
        Este método imprime la lista de nombres de matrices en la consola.
        """
        if self.matrix_names:
            print("Matrices disponibles:")
            for name in self.matrix_names:
                print(f"- {name}")
        else:
            print("No hay matrices disponibles.")

    def reduce_to_2d(self, matriz, axis):
        """
        Reduce una matriz a 2D promediando a lo largo del eje especificado.

        :param matriz: Matriz a reducir.
        :param axis: Eje a lo largo del cual promediar.
        :return: Matriz reducida a 2D.
        """
        return np.mean(matriz, axis=axis)

    def graficar_todos(self):
        """
        Grafica todos los datos: la señal EEG, el promedio en el eje 0 vs tiempo
        y el promedio en el eje 1 vs épocas (con recorte a las últimas 5 épocas),
        organizados según un diseño específico.
        """
        if not self.matrix_names:
            print("No hay matrices disponibles para graficar.")
            return

        matriz_nombre = self.matrix_names[0]
        matriz = self.get_matrix(matriz_nombre)

        if matriz is not None:
            num_canales, num_muestras, num_epocas = matriz.shape  # Se asume que la matriz tiene 3 dimensiones
            
            # Crear la figura y los ejes usando gridspec
            fig = plt.figure(figsize=(15, 10))
            gs = fig.add_gridspec(3, 3)  # Crear una cuadrícula de 3x3

            # 1. Gráfica de la señal EEG (canales vs tiempo, promediando sobre las épocas)
            matriz_2d = self.reduce_to_2d(matriz, axis=2)  # Reducir a 2D promediando sobre las épocas
            ax1 = fig.add_subplot(gs[1:3, 0:2])  # Subgráfico en la posición (2, 1) ocupando las dos columnas

            # Desplazamiento vertical para cada canal
            offset = 5  # Ajusta el desplazamiento según sea necesario
            for i in range(num_canales):
                ax1.plot(matriz_2d[i, :] + (i * offset), label=f'Canal {i + 1}')  # Sumar el desplazamiento vertical
            ax1.set_title(f"Señal EEG de '{matriz_nombre}' (Canales vs Tiempo)")
            ax1.set_xlabel("Muestras (Tiempo)")
            ax1.set_ylabel("Amplitud")
            ax1.legend(loc='upper right')

            # 2. Gráfico del promedio en el eje 0 vs tiempo
            ax2 = fig.add_subplot(gs[0, 2])  # Subgráfico en la posición (1, 3)
            promedio_tiempo = np.mean(matriz, axis=0)  # Promedio a lo largo de los canales
            ax2.plot(promedio_tiempo[:, 0], label='Promedio (Canales)', color='blue')
            ax2.set_title(f"Promedio de la señal EEG de '{matriz_nombre}' vs Tiempo")
            ax2.set_xlabel("Muestras (Tiempo)")
            ax2.set_ylabel("Amplitud (Promedio)")
            ax2.axhline(0, color='black', linewidth=0.5, linestyle='--')
            ax2.legend(loc='upper right')

            # 3. Gráfico del promedio en el eje 1 (canales) vs últimas 5 épocas
            ax3 = fig.add_subplot(gs[2, 2])  # Subgráfico en la posición (3, 3)
            if num_epocas >= 5:
                matriz_recortada = matriz[:, :, -5:]  # Recortar las últimas 5 épocas
                promedio_canales = np.mean(matriz_recortada, axis=1)  # Promediar a lo largo del tiempo
                for i in range(5):
                    ax3.plot(promedio_canales[:, i], label=f'Época {num_epocas - 5 + i + 1}')
            else:
                ax3.plot(np.mean(matriz, axis=1), label='Promedio (Todo)', color='orange')

            ax3.set_title(f"Promedio de la señal EEG de '{matriz_nombre}' vs Últimas 5 Épocas")
            ax3.set_xlabel("Canales")
            ax3.set_ylabel("Amplitud (Promedio)")
            ax3.axhline(0, color='black', linewidth=0.5, linestyle='--')
            ax3.legend(loc='upper right')

            plt.tight_layout()  # Ajustar el diseño para que no se superpongan
            plt.show()
        else:
            print(f"No se pudo graficar la matriz '{matriz_nombre}' porque no fue encontrada.")
    
    def graficar_ruido(self):
        if not self.matrix_names:
            print("No hay matrices disponibles para graficar.")
            return

        matriz_nombre = self.matrix_names[0]
        matriz = self.get_matrix(matriz_nombre)

        if matriz is not None:
            num_canales, num_muestras, num_epocas = matriz.shape  # Se asume que la matriz tiene 3 dimensiones

            # Solicitar 2 canales diferentes y 1 canal para el ruido
            try:
                canal1 = int(input("Ingrese el número del canal 1 (0 a {}): ".format(num_canales - 1)))
                canal2 = int(input("Ingrese el número del canal 2 (0 a {}): ".format(num_canales - 1)))
                canal_ruido = int(input("Ingrese el número del canal para agregar ruido (0 a {}): ".format(num_canales - 1)))

                if not all(0 <= canal < num_canales for canal in [canal1, canal2, canal_ruido]):
                    print("Los números de canal deben estar dentro del rango válido.")
                    return

            except ValueError:
                print("Entrada no válida. Asegúrese de ingresar números enteros.")
                return

            # Realizar operaciones entre los canales
            resta = matriz[canal1, :, :] - matriz[canal2, :, :]
            multiplicacion = matriz[canal1, :, :] * matriz[canal2, :, :]
            ruido = np.random.normal(0, 1, size=matriz[canal_ruido, :, :].shape)  # Agregar ruido al canal seleccionado
            canal_con_ruido = matriz[canal_ruido, :, :] + ruido

            # Crear la figura y los ejes usando gridspec
            fig = plt.figure(figsize=(15, 10))
            gs = fig.add_gridspec(3, 2)  # Crear una cuadrícula de 3 filas y 2 columnas

            # 1. Gráfica del canal con ruido ocupando las dos filas de la izquierda
            ax3 = fig.add_subplot(gs[0:2, 0])  # Subgráfico en las dos filas de la primera columna
            ax3.plot(canal_con_ruido[:, 0], label='Canal con Ruido', color='blue')
            ax3.set_title(f"Canal {canal_ruido + 1} con Ruido de '{matriz_nombre}' vs Tiempo")
            ax3.set_xlabel("Tiempo (segundos)")
            ax3.set_ylabel("Amplitud (Canal + Ruido)")
            ax3.axhline(0, color='black', linewidth=0.5, linestyle='--')
            ax3.legend(loc='upper right')

            # 2. Gráfica de la multiplicación vs tiempo (en la primera fila de la derecha)
            ax2 = fig.add_subplot(gs[0, 1])  # Subgráfico en la primera fila de la segunda columna
            ax2.plot(multiplicacion[:, 0], label='Multiplicación', color='green')
            ax2.set_title(f"Multiplicación entre Canales de '{matriz_nombre}' vs Tiempo")
            ax2.set_xlabel("Tiempo (segundos)")
            ax2.set_ylabel("Amplitud (Multiplicación)")
            ax2.axhline(0, color='black', linewidth=0.5, linestyle='--')
            ax2.legend(loc='upper right')

            # 3. Gráfica de la resta vs tiempo (en la segunda fila de la derecha)
            ax1 = fig.add_subplot(gs[1, 1])  # Subgráfico en la segunda fila de la segunda columna
            ax1.plot(resta[:, 0], label='Resta', color='red')
            ax1.set_title(f"Resta entre Canales de '{matriz_nombre}' vs Tiempo")
            ax1.set_xlabel("Tiempo (segundos)")
            ax1.set_ylabel("Amplitud (Resta)")
            ax1.axhline(0, color='black', linewidth=0.5, linestyle='--')
            ax1.legend(loc='upper right')

            plt.tight_layout()  # Ajustar el diseño para que no se superpongan
            plt.show()
        else:
            print(f"No se pudo graficar la matriz '{matriz_nombre}' porque no fue encontrada.")