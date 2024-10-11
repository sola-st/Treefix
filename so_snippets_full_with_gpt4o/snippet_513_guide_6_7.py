# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19339/transpose-unzip-function-inverse-of-zip
from l3.Runtime import _l_
def unzip(zipped):
    _l_(14073)

    """Inverse of built-in zip function.
    Args:
        zipped: a list of tuples

    Returns:
        a tuple of lists

    Example:
        a = [1, 2, 3]
        b = [4, 5, 6]
        zipped = list(zip(a, b))

        assert zipped == [(1, 4), (2, 5), (3, 6)]

        unzipped = unzip(zipped)

        assert unzipped == ([1, 2, 3], [4, 5, 6])

    """

    unzipped = ()
    _l_(14066)
    if len(zipped) == 0:
        _l_(14068)

        aux = unzipped
        _l_(14067)
        return aux

    dim = len(zipped[0])
    _l_(14069)

    for i in range(dim):
        _l_(14071)

        unzipped = unzipped + ([tup[i] for tup in zipped], )
        _l_(14070)
    aux = unzipped
    _l_(14072)

    return aux

