def P_C(graph):
    for vertex in graph:             # n-mal
        deg = 0
        for adj in vertex:           # (n-1)-mal
            deg +=1
        if deg != len(graph) - 1:
            return False
    return True
# wenn es keine Schleifen und keine Multikanten gibt, reicht es aus die adjazenten Knoten zu zählen
# jeder der n Knoten hat n - 1 adjazente Knoten
# => P_C löst in O(n*(n-1)) = O(n²) => C entscheidbar in polynomieller LZ

# g1 ist vollst Graph mit 4 Knoten
g1 = [
        [1, 2, 3],
        [0, 2, 3],
        [0, 1, 3],
        [0, 1, 2]
    ] 
g2 = [[1,2], [0]]

print(P_C(g2))