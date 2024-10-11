# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
from l3.Runtime import _l_
def find_dict_in_list(dicts, default=None, **kwargs):
    _l_(12957)

    """Find first matching :obj:`dict` in :obj:`list`.

    :param list dicts: List of dictionaries.
    :param dict default: Optional. Default dictionary to return.
        Defaults to `None`.
    :param **kwargs: `key=value` pairs to match in :obj:`dict`.

    :returns: First matching :obj:`dict` from `dicts`.
    :rtype: dict

    """

    rval = default
    _l_(12945)
    for d in dicts:
        _l_(12955)

        is_found = False
        _l_(12946)

        # Search for keys in dict.
        for k, v in kwargs.items():
            _l_(12951)

            if d.get(k, None) == v:
                _l_(12950)

                is_found = True
                _l_(12947)

            else:
                is_found = False
                _l_(12948)
                break
                _l_(12949)

        if is_found:
            _l_(12954)

            rval = d
            _l_(12952)
            break
            _l_(12953)
    aux = rval
    _l_(12956)

    return aux


if __name__ == '__main__':
    _l_(12977)

    # Tests
    dicts = []
    _l_(12958)
    keys = 'spam eggs shrubbery knight'.split()
    _l_(12959)

    start = 0
    _l_(12960)
    for _ in range(4):
        _l_(12964)

        dct = {k: v for k, v in zip(keys, range(start, start+4))}
        _l_(12961)
        dicts.append(dct)
        _l_(12962)
        start += 4
        _l_(12963)

    # Find each dict based on 'spam' key only.  
    for x in range(len(dicts)):
        _l_(12967)

        spam = x*4
        _l_(12965)
        assert find_dict_in_list(dicts, spam=spam) == dicts[x]
        _l_(12966)

    # Find each dict based on 'spam' and 'shrubbery' keys.
    for x in range(len(dicts)):
        _l_(12970)

        spam = x*4
        _l_(12968)
        assert find_dict_in_list(dicts, spam=spam, shrubbery=spam+2) == dicts[x]
        _l_(12969)

    # Search for one correct key, one incorrect key:
    for x in range(len(dicts)):
        _l_(12973)

        spam = x*4
        _l_(12971)
        assert find_dict_in_list(dicts, spam=spam, shrubbery=spam+1) is None
        _l_(12972)

    # Search for non-existent dict.
    for x in range(len(dicts)):
        _l_(12976)

        spam = x+100
        _l_(12974)
        assert find_dict_in_list(dicts, spam=spam) is None
        _l_(12975)

