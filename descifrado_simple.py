import re
from collections import Counter

def analizar_frecuencia(texto):
    """Analiza la frecuencia de las letras en el texto dado."""
    letras = re.findall(r'[A-Z]', texto.upper())
    total_letras = len(letras)
    frecuencia = Counter(letras)
    frecuencia_relativa = {letra: (conteo / total_letras) * 100 for letra, conteo in frecuencia.items()}
    return dict(sorted(frecuencia_relativa.items(), key=lambda item: item[1], reverse=True))

def actualizar_correspondencia(correspondencia, letra_cifrada, letra_descifrada):
    """Actualiza la correspondencia de descifrado según la elección del usuario."""
    correspondencia[letra_cifrada] = letra_descifrada.upper()

def descifrar_texto(texto, correspondencia):
    """Descifra el texto usando la correspondencia dada."""
    return ''.join([correspondencia.get(letra, letra) for letra in texto.upper()])

def programa_interactivo_descifrado():
    
    mensaje_cifrado = """PONER AQUI EL MENSAJE CIFRADO"""

    # Inicializar correspondencia
    correspondencia = {letra: letra for letra in set(re.findall(r'[A-Z]', mensaje_cifrado))}
    
   
    frecuencia_cifrado = analizar_frecuencia(mensaje_cifrado)
    
    # Mostrar la frecuencia de las letras 
    print("Frecuencia de letras en el mensaje cifrado:")
    for letra, frecuencia in frecuencia_cifrado.items():
        print(f'{letra}: {frecuencia:.2f}%')
    
    # Proceso interactivo de descifrado
    while True:
        print("\nTexto descifrado hasta ahora:")
        print(descifrar_texto(mensaje_cifrado, correspondencia))
        
        # Pedir el cambio
        letra_cifrada = input("\nIntroduce la letra cifrada que deseas reemplazar (o 'SALIR' para terminar): ").upper()
        if letra_cifrada == 'SALIR':
            break
        letra_descifrada = input(f"Introduce la letra por la que quieres reemplazar '{letra_cifrada}': ").upper()
        
        # Actualizar la correspondencia y mostrar el nuevo texto
        actualizar_correspondencia(correspondencia, letra_cifrada, letra_descifrada)


programa_interactivo_descifrado()

