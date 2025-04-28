import random  

def usar_la_fuerza(mochila, index=0):
    if index >= len(mochila):
        return False, index

    print(f"Usando la fuerza... revisando: {mochila[index]}")

    if mochila[index] == "sable de luz":
        return True, index + 1

    return usar_la_fuerza(mochila, index + 1)

mochila = ["comida", "botella", "capa", "comunicador", "sable de luz", "mapa estelar"]

random.shuffle(mochila)

print(f"Contenido de la mochila (desordenado): {mochila}\n")

encontrado, objetos_revisados = usar_la_fuerza(mochila)

if encontrado:
    print(f"\n¡Sable de luz encontrado! Se revisaron {objetos_revisados} objetos.")
else:
    print(f"\nNo se encontró ningún sable de luz. Se revisaron {objetos_revisados} objetos.")