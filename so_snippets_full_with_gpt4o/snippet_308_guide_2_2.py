# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list
from l3.Runtime import _l_
def getPermutations(array):
    _l_(14274)

    if len(array) == 1:
        _l_(14267)

        aux = [array]
        _l_(14266)
        return aux
    permutations = []
    _l_(14268)
    for i in range(len(array)):
        _l_(14272)

        # get all perm's of subarray w/o current item
        perms = getPermutations(array[:i] + array[i+1:])  
        _l_(14269)  
        for p in perms:
            _l_(14271)

            permutations.append([array[i], *p])
            _l_(14270)
    aux = permutations
    _l_(14273)
    return aux

def getPermutations(array):
    _l_(14281)

    if len(array) == 1:
        _l_(14280)

        yield array
        _l_(14275)
    else:
        for i in range(len(array)):
            _l_(14279)

            perms = getPermutations(array[:i] + array[i+1:])
            _l_(14276)
            for p in perms:
                _l_(14278)

                yield [array[i], *p]
                _l_(14277)

