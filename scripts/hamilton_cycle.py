# Zertifikat ist Knotenfolge c = (v1, ..., vi)
# P_HAM(G, c) liefert wahr wenn c ein Hamilton Kreis in Graph G = (V, E) ist, sonst falsch
def P_HAM(graph: list, certificate: tuple):

    start = certificate[0]
    certificate = list(certificate)
    certificate.append(start)
    print(certificate)

    visited = []                        
    idx_cert = 0

    for node in certificate:            # max. n = |V| Durchläufe, da visited max. n Einträge hat
        print(node)
        if node in visited:
            # kompletten graphen abgegangen und wieder am start?
            if len(certificate) - 1 == len(graph) and node is start:
                return True
            return False

        # wenn der nächste Knoten aus c von node aus erreichbar ist
        if certificate[idx_cert + 1] in graph[node]:
            idx_cert += 1
            visited.append(node)
        else:
            return False

# listenzugriff kann wie in einem C array als konstant angenommen werden
# => P_HAM verfiziert HAM in O(n) => HAM polynomiell verifizierbar

g1 = [
        [1, 2],
        [0, 2], 
        [0, 1]
    ]

g2 = [
        [1, 2, 3],
        [0, 2], 
        [0, 1, 3],
        [2, 0]
    ]

g3 = [
        [1, 2],
        [0, 2],
        [0, 1, 3],
        [2]
]

c1 = (2, 0, 1)
c2 = (0, 1, 2, 3)
c3 = (0, 2, 1, 3)

print(P_HAM(g1, c1)) # true
print(P_HAM(g2, c2)) # true
print(P_HAM(g3, c3)) # false