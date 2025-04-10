# 📊 Predicción de Movimientos de Buques con Machine Learning

Este proyecto aplica técnicas de **Aprendizaje Automático Supervisado** para analizar y predecir los movimientos de buques atracados en el **Puerto Exterior de A Coruña (Punta Langosteira)**. Utilizando datos meteorológicos y de atraque, se evalúa el impacto de diversas variables sobre los movimientos traslacionales y rotacionales de embarcaciones.

## 🧠 Objetivo del Proyecto

Determinar qué variables de entrada (meteorológicas y estructurales del barco) afectan en mayor medida los **6 grados de libertad** del movimiento de un buque:

- **Traslaciones**: Marejada (Surge), Ronza/Abatimiento (Sway), Arfada (Heave)
- **Rotaciones**: Escora (Roll), Cabeceo (Pitch), Guiñada (Yaw)

## 📁 Dataset

- Registro de 45 embarcaciones durante 3 años.
- Datos proporcionados por sistemas del puerto: estación meteorológica, boya de oleaje y mareógrafo.
- Variables de entrada: `Hs`, `Tp`, `Θm`, `Ws`, `Wd`, `H0`, `Hsm`, `length`, `breadth`, `dwt`.
- Variables de salida: `mov_avg`, `mov_max`, `mov_sig` para cada grado de libertad.

📌 Dataset original: [ship-movement-dataset](https://github.com/aalvarell/ship-movement-dataset)

## ⚙️ Algoritmos Aplicados

Se han utilizado tres modelos supervisados de regresión:

### 🔹 Regresión Lineal
- Modelo base para detectar relaciones lineales.
- Bajo rendimiento general (mejor R² ≈ 0.67).
- **Descartado.**

### 🔹 K-Vecinos más Cercanos (KNN)
- Modelo no lineal, captura mejor las relaciones complejas.
- R² promedio superior al de regresión lineal (mejor R² ≈ 0.89).
- **Descartado por no alcanzar valores cercanos a 1.**

### 🔹 Random Forest Regressor 🌲
- Mejor rendimiento general con R² cercano a 1.
- Permite evaluar la **importancia de cada variable**.
- **Modelo seleccionado.**

## 📌 Conclusiones Clave

- **Cabeceo (Pitch)**: influido principalmente por la **carga (dwt)** y longitud del buque.
- **Ronza/Abatimiento (Sway)**: influido por la **altura de ola (Hs)**.
- **Escora (Roll)**: afectada por la **longitud (length)**.
- **Marejada (Surge)**: dependiente del **tiempo entre olas (Tp)**.
- **Guiñada (Yaw)**: influida principalmente por la **manga o ancho del barco (breadth)**.

## 🛠️ Requisitos

- Python 3.x
- `pandas`, `numpy`, `matplotlib`, `sklearn`
- Google Colab (opcional, recomendado por su integración con Drive)

```bash
pip install pandas numpy matplotlib scikit-learn
```

## 📂 Estructura del Proyecto

```
/port_coruna/
│
├— heave_train.csv
├— pitch_train.csv
├— roll_train.csv
├— surge_train.csv
├— sway_train.csv
├— yaw_train.csv
└— (versiones *_test.csv para evaluación)
```

## 📊 Ejecución

Cada modelo puede ejecutarse en un entorno Jupyter Notebook o Google Colab. Los scripts están organizados por **tipo de movimiento** (heave, sway, pitch, etc.).

```python
# Entrenamiento Random Forest
model = RandomForestRegressor()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
```

## 📚 Bibliografía

- Módulo 4 del Máster en Data Science & Business Analytics – UCAV
- [Ship Movement Dataset](https://github.com/aalvarell/ship-movement-dataset)
- [Random Forest Regression – Towards Data Science](https://towardsdatascience.com/random-forest-regression-5f605132d19d)
- [Wikipedia – Movimiento y oscilación de un barco](https://es.wikipedia.org/wiki/Movimiento_y_oscilaci%C3%B3n_de_un_barco)
