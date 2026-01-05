cube_map = {}
cubes = [i**3 for i in range(0, 1001)]
#will have results from 0-1000, but now cubes[0] = 0 (unused), cubes[1] = 1, etc
for a in range(1, 1001):
    for b in range(a, 1001):
        result = cubes[a]+cubes[b]
        if result in cube_map:
            cube_map[result].append((a,b))
            for element in cube_map[result]: #for element in list of tuples
                if element != (a, b):
                    print(a, b, element[0], element[1]) #a, b, (THIS, x), (x, THIS) --> a, b, c, d
        else:
            cube_map[result] = [(a,b)]
