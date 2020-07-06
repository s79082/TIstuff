import sys

# Endzustaende
ends = ["zE", ]

# index: wert
delta = {"z0": {"a": "z1", "b": "z0", "c": "z0"},
        "z1": {"a": "z1", "b": "z2", "c": "z0"},
        "z2": {"a": "z1", "b": "z0", "c": "zE"},
        "zE": {"a": "zE", "b": "zE", "c": "zE"},
        }

def deltad(z, w):
    if len(w) == 0:
        print ("leer")
        return z
    else:
        first = w[0]
	# kopiere das restliche wort

    rest = w[1 : len(w)]
    next = delta[z][first]
    print ("(" + z +", "+ first + ") -> " + next)
    return deltad(next, rest)

def accepts(w):
    return deltad("z0", w) in ends

print (accepts(input()))
