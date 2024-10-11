# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
from l3.Runtime import _l_
def find_dict_in_list(dicts, default=None, **kwargs):
    _l_(3318)

    """Find first matching :obj:`dict` in :obj:`list`.

    :param list dicts: List of dictionaries.
    :param dict default: Optional. Default dictionary to return.
        Defaults to `None`.
    :param **kwargs: `key=value` pairs to match in :obj:`dict`.

    :returns: First matching :obj:`dict` from `dicts`.
    :rtype: dict

    """

    rval = default
    _l_(3306)
    for d in dicts:
        _l_(3316)

        is_found = False
        _l_(3307)

        # Search for keys in dict.
        for k, v in kwargs.items():
            _l_(3312)

            if d.get(k, None) == v:
                _l_(3311)

                is_found = True
                _l_(3308)

            else:
                is_found = False
                _l_(3309)
                break
                _l_(3310)

        if is_found:
            _l_(3315)

            rval = d
            _l_(3313)
            break
            _l_(3314)
    aux = rval
    _l_(3317)

    return aux


if __name__ == '__main__':
    _l_(3338)

    # Tests
    dicts = []
    _l_(3319)
    keys = 'spam eggs shrubbery knight'.split()
    _l_(3320)

    start = 0
    _l_(3321)
    for _ in range(4):
        _l_(3325)

        dct = {k: v for k, v in zip(keys, range(start, start+4))}
        _l_(3322)
        dicts.append(dct)
        _l_(3323)
        start += 4
        _l_(3324)

    # Find each dict based on 'spam' key only.  
    for x in range(len(dicts)):
        _l_(3328)

        spam = x*4
        _l_(3326)
        assert find_dict_in_list(dicts, spam=spam) == dicts[x]
        _l_(3327)

    # Find each dict based on 'spam' and 'shrubbery' keys.
    for x in range(len(dicts)):
        _l_(3331)

        spam = x*4
        _l_(3329)
        assert find_dict_in_list(dicts, spam=spam, shrubbery=spam+2) == dicts[x]
        _l_(3330)

    # Search for one correct key, one incorrect key:
    for x in range(len(dicts)):
        _l_(3334)

        spam = x*4
        _l_(3332)
        assert find_dict_in_list(dicts, spam=spam, shrubbery=spam+1) is None
        _l_(3333)

    # Search for non-existent dict.
    for x in range(len(dicts)):
        _l_(3337)

        spam = x+100
        _l_(3335)
        assert find_dict_in_list(dicts, spam=spam) is None
        _l_(3336)

