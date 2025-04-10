El siguiente proyecto resuelve un caso prác@co de Aprendizaje Automá@co Supervisado, empleando el lenguaje de programación Python. El conjunto de datos empleado, disponible en la bibliograIa del documento, muestra los movimientos de 45 embarcaciones marí@mas registrados en el Puerto Exterior de A Coruña (Punta Langosteira), Galicia, España, en dis@ntas fechas y en un periodo de @empo de 3 años. Cada archivo con@ene variables de @po predictoras (de entrada) y variables a predecir (de salida). Es importante destacar que las caracterís@cas geométricas de un barco inciden de manera directa en el comportamiento dinámico del mismo, y que en el archivo original se muestra el día y la hora exactos correspondientes a cada movimiento grabado.
1.1 Obje(vo
Dado un conjunto de datos obtenidos de forma experimental, teniendo variables de entrada (meteorológicas y de atraque de cada buque), el obje@vo es determinar qué variable afecta en mayor magnitud a cada movimiento, tanto traslacional como rotacional, de un buque atracado en puerto. Para ello, se han empleado 3 Algoritmos de Aprendizaje Supervisado: Regresión Lineal, K-Vecinos más cercanos o KNN y el algoritmo ensamblado ‘Random Forest’, basado en algoritmos simples de árboles de decisión. En la tabla e ilustración de a con@nuación se observan los grados de libertad desde un punto de vista más ilustra@vo.
Tabla 1. Grados de libertad de un buque
  Traslaciones
Avance, Retroceso o Marejada (x) Ronza o Aba@miento (y) Ascenso, Descenso o Arfada (z)
Rotaciones
Escora o Balance (x) Cabeceo (y) Virada o Guiñada (z)
