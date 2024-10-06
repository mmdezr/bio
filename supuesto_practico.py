import os
import numpy as np
from hmmlearn import hmm
from Bio import SeqIO


# Función para cargar secuencias de proteínas desde múltiples archivos FASTA
def cargar_secuencias_proteinas(directorio):
    secuencias_proteinas = []
    for archivo in os.listdir(directorio):
        if archivo.endswith(".fasta") or archivo.endswith(".fa"):
            ruta_archivo = os.path.join(directorio, archivo)
            for record in SeqIO.parse(ruta_archivo, "fasta"):
                secuencia = [
                    convertir_aminoacido_a_numero(aa) for aa in str(record.seq)
                ]
                secuencias_proteinas.append(secuencia)
    return secuencias_proteinas


# Función para convertir aminoácidos en números
def convertir_aminoacido_a_numero(aminoacido):
    conversion = {
        "A": 0,
        "C": 1,
        "D": 2,
        "E": 3,
        "F": 4,
        "G": 5,
        "H": 6,
        "I": 7,
        "K": 8,
        "L": 9,
        "M": 10,
        "N": 11,
        "P": 12,
        "Q": 13,
        "R": 14,
        "S": 15,
        "T": 16,
        "V": 17,
        "W": 18,
        "Y": 19,
    }
    return conversion.get(
        aminoacido, -1
    )  # Convertir a -1 si el aminoácido no es válido


# Cargar todas las secuencias de proteínas desde los archivos FASTA
directorio = "/ruta/proteins"
secuencias_proteinas = cargar_secuencias_proteinas(directorio)

# Preparar los datos para el entrenamiento del HMM
X = np.concatenate(secuencias_proteinas)
lengths = [len(seq) for seq in secuencias_proteinas]

# Definir y entrenar el modelo HMM con 3 estados
num_estados = 3
num_features = 20  # Número de posibles aminoácidos (20 diferentes)

# Configurar el modelo MultinomialHMM sin inicializar manualmente
modelo_hmm = hmm.MultinomialHMM(n_components=num_estados, random_state=42, n_iter=100)

# Entrenar el modelo HMM
modelo_hmm.fit(X.reshape(-1, 1), lengths)

# Clasificar una nueva secuencia de proteínas
nueva_secuencia = np.array([convertir_aminoacido_a_numero(aa) for aa in "MCSPCV"])
logprob, estados_ocultos = modelo_hmm.decode(
    nueva_secuencia.reshape(-1, 1), algorithm="viterbi"
)

print("Log-probabilidad de la secuencia:", logprob)
print("Estados ocultos predichos:", estados_ocultos)

# Mostrar el estado oculto asignado para cada secuencia
for i, secuencia in enumerate(secuencias_proteinas):
    _, estados = modelo_hmm.decode(
        np.array(secuencia).reshape(-1, 1), algorithm="viterbi"
    )
    print(f"Secuencia {i+1}: Estados Ocultos {estados}")
