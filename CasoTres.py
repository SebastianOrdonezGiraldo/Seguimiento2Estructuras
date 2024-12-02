# Diccionario de notas
notas = {
    "Calculo": {"pp": 3.5, "sp": 2.5, "tp": 1.5},
    "Química": {"pp": 2.5, "sp": 3.0, "tp": 5.0},
    "Deporte": {"pp": 2.4, "sp": 2.0, "tp": 2.2},
    "Lógica": {"pp": 1.5, "sp": 4.0, "tp": 4.5}
}

# 3.1 Función para calcular la nota final de cada materia
def c31_final():
    for materia, calificaciones in notas.items():
        # Cálculo de la nota final
        nota_final = (calificaciones["pp"] * 0.3) + (calificaciones["sp"] * 0.3) + (calificaciones["tp"] * 0.4)
        # Agregar la nota final al subdiccionario
        calificaciones["final"] = nota_final

# 3.2 Función para calcular el promedio de las notas finales
def c32_promedio():
    suma_notas_finales = 0
    for calificaciones in notas.values():
        # Acceder a la nota final en el subdiccionario
        suma_notas_finales += calificaciones["final"]
    # Calcular el promedio dividiendo entre el número de materias
    promedio = suma_notas_finales / len(notas)
    return promedio

# Llamar las funciones
c31_final()  # Calcula las notas finales y actualiza el diccionario
promedio = c32_promedio()  # Calcula el promedio general

# Mostrar resultados
print("Materias con notas finales:")
for materia, calificaciones in notas.items():
    print(f"{materia}: {calificaciones}")
print(f"Promedio del estudiante: {promedio:.2f}")
