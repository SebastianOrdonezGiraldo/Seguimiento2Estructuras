# Lista de notas
notas = [
    ["Calculo", 3.5, 2.5, 1.5],
    ["Química", 2.5, 3.0, 5.0],
    ["Deporte", 2.4, 2.0, 2.2],
    ["Lógica", 1.5, 4.0, 4.5]
]

# 1.1 Función para calcular la nota final de cada materia
def c11_final():
    for materia in notas:
        # Cálculo de la nota final
        nota_final = (materia[1] * 0.3) + (materia[2] * 0.3) + (materia[3] * 0.4)
        # Agregar la nota final a la sublista de la materia
        materia.append(nota_final)

# 1.2 Función para calcular el promedio de las notas finales
def c12_promedio():
    suma_notas_finales = 0
    for materia in notas:
        # La nota final está en la última posición de cada sublista
        suma_notas_finales += materia[-1]
    # Calcular el promedio dividiendo entre el número de materias
    promedio = suma_notas_finales / len(notas)
    return promedio

# Llamar las funciones
c11_final()  # Calcula las notas finales y actualiza la lista
promedio = c12_promedio()  # Calcula el promedio general

# Mostrar resultados
print("Materias con notas finales:")
for materia in notas:
    print(materia)
print(f"Promedio del estudiante: {promedio:.2f}")
