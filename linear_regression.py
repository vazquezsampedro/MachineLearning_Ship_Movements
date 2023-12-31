# -*- coding: utf-8 -*-
"""Linear_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11jSgWMTAwftpICMg-PRmUlxTOzBkj7s8
"""

# Commented out IPython magic to ensure Python compatibility.
# MODELO DE APRENDIZAJE AUTOMÁTICO SUPERVISADO / ALGORITMO DE REGRESIÓN LINEAL
# 1) Oscilación eje Z (heave)
# Se accede a las carpetas de Google Drive y se habilta la entrada de código
from google.colab import drive
drive.mount('/content/drive')
from ast import Mult
# Se habilitan gráficos dentro de Jupyter Notebook
# %matplotlib inline

# Se importan las librerías para el acceso al dataset
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Se accede al archivo CSV
heave_train = '/content/drive/MyDrive/port_coruna/heave_train.csv'
df = pd.read_csv(heave_train)
x = df[['h_s', 't_p', 'dir', 'wind_speed', 'wind_dir', 'h_0', 'h_sm', 'length', 'breath']]
y = df[['mov_avg','mov_max','mov_sig']]

# Se crea la instancia (objeto específico del modelo) y se ajusta el modelo a los datos
model = LinearRegression()
model.fit(x, y)
prediction_linear = model.predict(x)
r2 = r2_score(y, prediction_linear)

# Se realizan predicciones del modelo y se muestra

plt.scatter(y, prediction_linear)
plt.xlabel('Oscilación vertical lineal de la embarcación (real)')
plt.ylabel('Oscilación vertical lineal de la embarcación (Predicción)')
plt.show()
print("coeficientes:", model.coef_)
print("Termino independiente:", model.intercept_)
print(r2)

# Commented out IPython magic to ensure Python compatibility.
# MODELO DE APRENDIZAJE AUTOMÁTICO SUPERVISADO / ALGORITMO DE REGRESIÓN LINEAL
# 2) Guiñada, rotación del buque (eje Z)
# Se accede a las carpetas de Google Drive y se habilta la entrada de código
from google.colab import drive
drive.mount('/content/drive')
from ast import Mult
# Se habilitan gráficos dentro de Jupyter Notebook
# %matplotlib inline

# Se importan las librerías para el acceso al dataset
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Se accede al archivo CSV
yaw_train = '/content/drive/MyDrive/port_coruna/yaw_train.csv'
df = pd.read_csv(yaw_train)
x = df[['h_s', 't_p', 'dir', 'wind_speed', 'wind_dir', 'h_0', 'h_sm', 'length', 'breath']]
y = df[['mov_avg','mov_max','mov_sig']]

# Se crea la instancia (objeto específico del modelo) y se ajusta el modelo a los datos
model = LinearRegression()
model.fit(x, y)
prediction_linear = model.predict(x)
r2 = r2_score(y, prediction_linear)

# Se realizan predicciones del modelo y se muestra

plt.scatter(y, prediction_linear)
plt.xlabel('Guiñada de la embarcacion (real)')
plt.ylabel('Guiñada de la embarcación (Predicción)')
plt.show()
print("coeficientes:", model.coef_)
print("Termino independiente:", model.intercept_)
print(r2)

# Commented out IPython magic to ensure Python compatibility.
# MODELO DE APRENDIZAJE AUTOMÁTICO SUPERVISADO / ALGORITMO DE REGRESIÓN LINEAL
# 3) Marejada, movimiento longitudinal lineal (eje x)
# Se accede a las carpetas de Google Drive y se habilta la entrada de código
from google.colab import drive
drive.mount('/content/drive')
from ast import Mult
# Se habilitan gráficos dentro de Jupyter Notebook
# %matplotlib inline

# Se importan las librerías para el acceso al dataset
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Se accede al archivo CSV
surge_train = '/content/drive/MyDrive/port_coruna/surge_train.csv'
df = pd.read_csv(surge_train)
x = df[['h_s', 't_p', 'dir', 'wind_speed', 'wind_dir', 'h_0', 'h_sm', 'length', 'breath']]
y = df[['mov_avg','mov_max','mov_sig']]

# Se crea la instancia (objeto específico del modelo) y se ajusta el modelo a los datos
model = LinearRegression()
model.fit(x, y)
prediction_linear = model.predict(x)
r2 = r2_score(y, prediction_linear)

# Se realizan predicciones del modelo y se muestra

plt.scatter(y, prediction_linear)
plt.xlabel('Marejada de la embarcacion (real)')
plt.ylabel('Marejada de la embarcación (Predicción)')
plt.show()
print("coeficientes:", model.coef_)
print("Termino independiente:", model.intercept_)
print(r2)

# Commented out IPython magic to ensure Python compatibility.
# MODELO DE APRENDIZAJE AUTOMÁTICO SUPERVISADO / ALGORITMO DE REGRESIÓN LINEAL
# 4) Balanceo basculante del buque (eje x)
# Se accede a las carpetas de Google Drive y se habilta la entrada de código
from google.colab import drive
drive.mount('/content/drive')
from ast import Mult
# Se habilitan gráficos dentro de Jupyter Notebook
# %matplotlib inline

# Se importan las librerías para el acceso al dataset
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Se accede al archivo CSV
roll_train = '/content/drive/MyDrive/port_coruna/roll_train.csv'
df = pd.read_csv(roll_train)
x = df[['h_s', 't_p', 'dir', 'wind_speed', 'wind_dir', 'h_0', 'h_sm', 'length', 'breath']]
y = df[['mov_avg','mov_max','mov_sig']]

# Se crea la instancia (objeto específico del modelo) y se ajusta el modelo a los datos
model = LinearRegression()
model.fit(x, y)
prediction_linear = model.predict(x)
r2 = r2_score(y, prediction_linear)

# Se realizan predicciones del modelo y se muestra

plt.scatter(y, prediction_linear)
plt.xlabel('Escora o Balanceo de la embarcacion (real)')
plt.ylabel('Escora o Balanceo de la embarcación (Predicción)')
plt.show()
print("coeficientes:", model.coef_)
print("Termino independiente:", model.intercept_)
print(r2)

# Commented out IPython magic to ensure Python compatibility.
# MODELO DE APRENDIZAJE AUTOMÁTICO SUPERVISADO / ALGORITMO DE REGRESIÓN LINEAL
# 5) Abatimiento, movimiento lateral lineal (eje y)
# Se accede a las carpetas de Google Drive y se habilta la entrada de código
from google.colab import drive
drive.mount('/content/drive')
from ast import Mult
# Se habilitan gráficos dentro de Jupyter Notebook
# %matplotlib inline

# Se importan las librerías para el acceso al dataset
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Se accede al archivo CSV
sway_train = '/content/drive/MyDrive/port_coruna/sway_train.csv'
df = pd.read_csv(sway_train)
df.dropna(inplace= True)
x = df[['h_s', 't_p', 'dir', 'wind_speed', 'wind_dir', 'h_0', 'h_sm', 'length', 'breath']]
y = df[['mov_avg','mov_max','mov_sig']]

# Se crea la instancia (objeto específico del modelo) y se ajusta el modelo a los datos
model = LinearRegression()
model.fit(x, y)
prediction_linear = model.predict(x)
r2 = r2_score(y, prediction_linear)

# Se realizan predicciones del modelo y se muestra

plt.scatter(y, prediction_linear)
plt.xlabel('Balanceo lateral lineal de la embarcacion (real)')
plt.ylabel('Balanceo lateral lineal de la embarcación (Predicción)')
plt.show()
print("coeficientes:", model.coef_)
print("Termino independiente:", model.intercept_)
print(r2)

# Commented out IPython magic to ensure Python compatibility.
# MODELO DE APRENDIZAJE AUTOMÁTICO SUPERVISADO / ALGORITMO DE REGRESIÓN LINEAL
# 6) Cebeceo, rotación ascendente / descendente del buque (eje y)
# Se accede a las carpetas de Google Drive y se habilta la entrada de código
from google.colab import drive
drive.mount('/content/drive')
from ast import Mult
# Se habilitan gráficos dentro de Jupyter Notebook
# %matplotlib inline

# Se importan las librerías para el acceso al dataset
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Se accede al archivo CSV
pitch_train = '/content/drive/MyDrive/port_coruna/pitch_train.csv'
df = pd.read_csv(pitch_train)
x = df[['h_s', 't_p', 'dir', 'wind_speed', 'wind_dir', 'h_0', 'h_sm', 'length', 'breath']]
y = df[['mov_avg','mov_max','mov_sig']]

# Se crea la instancia (objeto específico del modelo) y se ajusta el modelo a los datos
model = LinearRegression()
model.fit(x, y)
prediction_linear = model.predict(x)
r2 = r2_score(y, prediction_linear)

# Se realizan predicciones del modelo y se muestra

plt.scatter(y, prediction_linear)
plt.xlabel('Cabeceo ascendente/descendente eje lateral buque (real)')
plt.ylabel('Cabeceo ascendente/descendente eje lateral buque (Predicción)')
plt.show()
print("coeficientes:", model.coef_)
print("Termino independiente:", model.intercept_)
print(r2)