# 1. NUESTROS DATOS (Mensajes de prueba)
correos_nuevos = [
    "Hola, ¿vamos por unos tacos saliendo de la escuela",
    "¡URGENTE! Gana dinero rápido desde casa dando clic",
    "Recuerda que mañana es el examen de Inteligencia A",
    "Felicidades, ganaste un premio gratis, da clic ya",
    "No te pierdas hasta 31% de descuento",
    "Ha recibido 1,700 pesos",
    "Oferta exclusiva solo por hoy",
    "Felicidades, fuiste seleccionado para un premio exclusivo",
    "Se agrego un comentario",
    "Reclama tu regalo antes de que expire"
]
# 2. NUESTRO MODELO (Entrenamiento/Reglas)
# El modelo "aprende" que estas palabras suelen ser de spam
palabras_spam = ["gratis", "ganaste", "clic", "dinero"]

def modelo_ia_filtro(correo):
    # Convertimos a minúsculas para que no afecten las mayúsculas
    correo_minuscula = correo.lower()

    # El modelo busca si alguna palabra sospechosa está
    for palabra in list(palabras_spam):
        if palabra in correo_minuscula:
            return "SPAM"  # Predicción 1

    return "CORREO DESEADO"  # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("---- EJECUTANDO NUESTRA IA ----")
for i, correo in enumerate(correos_nuevos, 1):
    prediccion = modelo_ia_filtro(correo)
    print(f"Correo {i}: '{correo}' -> PREDICCIÓN DE LA IA: {prediccion}")
