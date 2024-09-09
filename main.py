
import heapq
import math

# Coordenadas (latitud, longitud) para cada nodo
coordenadas = {
    0: (-12.073473758029936, -76.952624367155),  # A
    1: (-12.070588857547358, -76.95329198329539),  # C
    2: (-12.069741908387785, -76.95388742471789),  # D
    3: (-12.069441946585137, -76.95333709249405),  # E
    4: (-12.073297312409203, -76.95050423481726),  # F
    5: (-12.072785619451846, -76.95058543137489),  # G
    6: (-12.070968219323593, -76.95104554520137),  # H
    7: (-12.069927178745205, -76.95141544063051),  # I
    8: (-12.068974358399558, -76.95171316134176),  # J
    9: (-12.069141984446699, -76.952317624604),  # K
    10: (-12.072644462601943, -76.95002607731132),  # L
    11: (-12.071356402910688, -76.95028771066363),  # M
    12: (-12.070800594418937, -76.95049521297753),  # N
    13: (-12.069706618781375, -76.9508741302464),  # O
    14: (-12.068762620084861, -76.95114478543846),  # P
    15: (-12.068250918466983, -76.94947574508748),  # Q
    16: (-12.071232890012174, -76.94950281060669),  # R
    17: (-12.073050288344927, -76.94876301974841),  # S
    18: (-12.071418159338597, -76.94889834734444),  # T
    19: (-12.070906462791973, -76.94877204158814),  # U
    20: (-12.069027292952082, -76.94861867031265),  # V
    21: (-12.068515591839594, -76.94876301974841)  # W
}

# Definición del grafo como una matriz de adyacencia
grafo = [
    [0, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
    [5, 0, 4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
    [0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # E
    [3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],  # F
    [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
    [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # H
    [0, 5, 0, 0, 0, 0, 2, 0, 4, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],  # I
    [0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # J
    [0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # K
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],  # L
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # M
    [0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0],  # N
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 5, 0],  # O
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],  # P
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],  # Q
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # R
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],  # S
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0],  # T
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0],  # U
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 4],  # V
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],  # W
]


# Función para calcular la distancia de Haversine
def haversine(coord1, coord2):
    R = 6371.0  # Radio de la Tierra en kilómetros
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return distancia


# Heurística basada en la distancia de Haversine
def heuristica(a, b):
    return haversine(coordenadas[a], coordenadas[b])


# Algoritmo A* con la nueva heurística
def a_estrella(grafo, inicio, final):
    cola = []
    heapq.heappush(cola, (0, inicio))

    costo = {inicio: 0}
    caminos = {inicio: None}

    while cola:
        costo1, vertice_actual = heapq.heappop(cola)

        if vertice_actual == final:
            camino = []
            while vertice_actual is not None:
                camino.append(vertice_actual)
                vertice_actual = caminos[vertice_actual]
            camino.reverse()
            return camino

        for V_vecino, peso in enumerate(grafo[vertice_actual]):
            if peso > 0:
                nuevo_costo = costo[vertice_actual] + peso
                if V_vecino not in costo or nuevo_costo < costo[V_vecino]:
                    costo[V_vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(final, V_vecino)
                    heapq.heappush(cola, (prioridad, V_vecino))
                    caminos[V_vecino] = vertice_actual

    return None


# Función para convertir índices a letras
def convertir_letras(camino):
    letras_a_indexar = "ACDEFGHIJKLMNOPQRSTUVW"
    return [letras_a_indexar[vertice] for vertice in camino]


# Definir los nodos de inicio y fin
inicio = 0  # Nodo A
final = 21  # Nodo W

# Ejecutar el algoritmo
camino = a_estrella(grafo, inicio, final)

# Mostrar la ruta encontrada
print("Ruta más corta de A a W (Indices):", camino)
print("Ruta más corta de A a W (Vertices o nodos):", convertir_letras(camino))
