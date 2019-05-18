# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
sb = search.GPSProblem('S', 'B', search.romania)

print('###############################')


print('1.Busqueda en anchura Bucharest Arad')
print(search.breadth_first_graph_search(ab).path())
print('2.Busqueda en profundidad Bucharest Arad')
print(search.depth_first_graph_search(ab).path())
print('3.Busqueda en acotacion y ramificacion (distancia acumulada) Bucharest Arad')
print(search.coste_acumulado(ab).path())
print('4.Busqueda heuristica Bucharest Arad')
print(search.coste_heuristico(ab).path())

print('###############################')

print('1.Busqueda en anchura Bucharest Sidiu')
print(search.breadth_first_graph_search(sb).path())
print('2.Busqueda en profundidad Bucharest Sidiu')
print(search.depth_first_graph_search(sb).path())
print('3.Busqueda en acotacion y ramificacion (distancia acumulada) Bucharest Sidiu')
print(search.coste_acumulado(sb).path())
print('4.Busqueda heuristica Bucharest Sidiu')
print(search.coste_heuristico(sb).path())
print('###############################')

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
