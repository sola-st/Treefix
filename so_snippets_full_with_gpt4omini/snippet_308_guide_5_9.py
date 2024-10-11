# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list
from l3.Runtime import _l_
def getPermutations(array):
    _l_(2509)

    if len(array) == 1:
        _l_(2502)

        aux = [array]
        _l_(2501)
        return aux
    permutations = []
    _l_(2503)
    for i in range(len(array)):
        _l_(2507)

        # get all perm's of subarray w/o current item
        perms = getPermutations(array[:i] + array[i+1:])  
        _l_(2504)  
        for p in perms:
            _l_(2506)

            permutations.append([array[i], *p])
            _l_(2505)
    aux = permutations
    _l_(2508)
    return aux

def getPermutations(array):
    _l_(2516)

    if len(array) == 1:
        _l_(2515)

        yield array
        _l_(2510)
    else:
        for i in range(len(array)):
            _l_(2514)

            perms = getPermutations(array[:i] + array[i+1:])
            _l_(2511)
            for p in perms:
                _l_(2513)

                yield [array[i], *p]
                _l_(2512)

