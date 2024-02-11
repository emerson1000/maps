import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Obtener el grafo de la red de carreteras de cualquier ciudad
G = ox.graph_from_place('Los Ángeles, Chile', network_type='drive')

# Mostrar el mapa de la ciudad escogida
ox.plot_graph(G, node_size=0, edge_color='b', close=False)

# Función para encontrar la ruta entre dos puntos
def find_route(G, origin, destination):
    origin_node = ox.nearest_nodes(G, origin[1], origin[0])
    destination_node = ox.nearest_nodes(G, destination[1], destination[0])
    route = nx.shortest_path(G, origin_node, destination_node, weight='length')
    return route

# Coordenadas aleatorias
origin = (-37,4629159, -72,3612251)
destination = (-34,549076, -118,242643)

# Encontrar la ruta entre las coordenadas
route = find_route(G, origin, destination)

# Mostrar la ruta en el mapa
ox.plot_graph_route(G, route, route_linewidth=6, node_size=0, edge_color='r', close=False)

# Mostrar el mapa completo con la ruta
plt.show()
