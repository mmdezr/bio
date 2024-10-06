# Proyecto de Clasificación de Secuencias de Proteínas con Modelos Ocultos de Markov (HMM)

## Descripción

Este proyecto tiene como objetivo implementar un **modelo de clasificación** para secuencias de proteínas utilizando **Modelos Ocultos de Markov** (HMM). El código carga secuencias de proteínas desde archivos en formato FASTA, las convierte en secuencias numéricas basadas en sus aminoácidos y entrena un modelo HMM para identificar los estados ocultos asociados con cada secuencia.

El enfoque principal se centra en la clasificación de secuencias en **estados ocultos**, basándose en los patrones observados dentro de las secuencias de proteínas. Además, se ha probado con distintos números de estados ocultos (dos, tres, cuatro y cinco) para determinar cuál es el más adecuado según la **log-probabilidad** resultante de las predicciones.

### Apartados Abordados:

- **Carga y procesamiento de datos**: Se leen secuencias de proteínas de archivos FASTA y se transforman en secuencias numéricas.
- **Entrenamiento del modelo HMM**: Utilizando el algoritmo Viterbi para predecir los estados ocultos de las secuencias de proteínas.
- **Evaluación del modelo**: Mediante la **log-probabilidad**, se mide la eficacia del modelo para diferentes configuraciones de estados ocultos.

## Tecnologías Usadas

- **Python**: El lenguaje principal del proyecto, ideal para manipular datos y entrenar modelos de machine learning.
- **hmmlearn**: Esta librería se utilizó para implementar el modelo HMM debido a su flexibilidad en la creación de modelos secuenciales con componentes ocultos.
- **Biopython**: Utilizada para manejar archivos FASTA, facilitando la extracción y procesamiento de secuencias biológicas.
- **NumPy**: Para operaciones numéricas eficientes, como la conversión de secuencias de proteínas en formatos adecuados para el modelo.

Cada herramienta fue seleccionada por su capacidad para manejar de manera eficiente las operaciones específicas necesarias para procesar datos biológicos y entrenar modelos de clasificación.

## Razonamiento

La elección de un **modelo oculto de Markov (HMM)** es adecuada para este tipo de problemas porque las secuencias de proteínas son **series temporales** con patrones subyacentes que no son observables directamente. Los HMM son especialmente útiles cuando se quiere modelar un sistema donde se tienen secuencias observables que dependen de estados ocultos, como es el caso de las proteínas, donde los aminoácidos observados están influenciados por un conjunto de estados ocultos (estructuras o funcionalidades no observables directamente).

En este proyecto, el uso de HMM permitió la clasificación de secuencias de proteínas en estados ocultos, lo que es crucial para entender mejor los patrones biológicos que rigen la estructura y función de las proteínas. Además, se comprobó que el uso de tres estados ocultos proporciona una mejor **log-probabilidad** que el uso de dos, cuatro o cinco, lo que sugiere que el modelo con más estados captura de manera más precisa la complejidad de las secuencias.

En resumen, el enfoque implementado es adecuado porque permite analizar las secuencias de proteínas desde una perspectiva probabilística, capturando la naturaleza secuencial y oculta de las proteínas.
