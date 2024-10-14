import pandas as pd
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

class Read_CSV:
  """
  Clase para manipular archivos CSV.
  """
  def __init__(self, file_path):
    self.file_path = file_path
    self.data = None

  def load_csv(self):
    """
    Carga el archivo CSV en un DataFrame de Pandas.
    """
    self.data = pd.read_csv(self.file_path, index_col=0)

  def display_data(self):
    """
    Muestra los datos cargados.
    """
    if self.data is not None:
      print(self.data)
    else:
      print("No se han cargado datos.")


class Read_Mat:
  """
  Clase para manipular archivos MAT.
  """
  def __init__(self, file_path):
    self.file_path = file_path
    self.data = None

  def load_mat(self):
    """
    Carga el archivo MAT en un diccionario de Python.
    """
    self.data = sio.loadmat(self.file_path)

  def reshape(self, matrix_name):
    """
    Modifica una matriz del archivo MAT a 2D.
    """
    if self.data is not None:
      if matrix_name in self.data:
        matrix = self.data[matrix_name]
        if len(matrix.shape) > 2:
          self.data[matrix_name] = matrix.reshape(-1, matrix.shape[-1])
          print(f"Matriz '{matrix_name}' modificada a 2D.")
        else:
          print(f"La matriz '{matrix_name}' ya es 2D.")
      else:
        print(f"No se encontró la matriz '{matrix_name}'.")
    else:
      print("No se han cargado datos.")

  def display_data(self):
    """
    Muestra los datos cargados del archivo mat.
    """
    if self.data is not None:
      for key, value in self.data.items():
          if isinstance(value, np.ndarray):
              print(f"Matriz '{key}':\n {value}")
          else:
              print(f"Variable '{key}':\n {value}")
    else:
      print("No se han cargado datos.")



# Crear una instancia de la clase Read_CSV para leer un archivo llamado "datos.csv"
lector_csv = Read_CSV(r"C:\Users\VICTUS\Desktop\UdeA\Cuarto Semestre\Informática 2\Parcial 2\Parcial 2\cancer patient data sets.csv")

# Cargar los datos del archivo CSV
lector_csv.load_csv()

# Mostrar los datos cargados
lector_csv.display_data()


# Crear una instancia de la clase Read_Mat para leer un archivo llamado "datos.mat"
lector_mat = Read_Mat(r"C:\Users\VICTUS\Desktop\UdeA\Cuarto Semestre\Informática 2\Parcial 2\Parcial 2\S1.mat")

# Cargar los datos del archivo MAT
lector_mat.load_mat()

# # Modificar una matriz llamada "matriz_ejemplo" a 2D
# lector_mat.reshape("matriz_ejemplo")

# Mostrar los datos cargados
lector_mat.display_data()