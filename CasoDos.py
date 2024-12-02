# Diccionario de notas
notas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Química": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Lógica": [1.5, 4.0, 4.5]
}

# 2.1 Función para calcular la nota final de cada materia
def c21_final():
    for materia, calificaciones in notas.items():
        # Cálculo de la nota final
        nota_final = (calificaciones[0] * 0.3) + (calificaciones[1] * 0.3) + (calificaciones[2] * 0.4)
        # Agregar la nota final a la lista de calificaciones
        calificaciones.append(nota_final)

# 2.2 Función para calcular el promedio de las notas finales
def c22_promedio():
    suma_notas_finales = 0
    for calificaciones in notas.values():
        # La nota final está en la última posición de cada lista
        suma_notas_finales += calificaciones[-1]
    # Calcular el promedio dividiendo entre el número de materias
    promedio = suma_notas_finales / len(notas)
    return promedio

# Llamar las funciones
c21_final()  # Calcula las notas finales y actualiza el diccionario
promedio = c22_promedio()  # Calcula el promedio general

# Mostrar resultados
print("Materias con notas finales:")
for materia, calificaciones in notas.items():
    print(f"{materia}: {calificaciones}")
print(f"Promedio del estudiante: {promedio:.2f}")
