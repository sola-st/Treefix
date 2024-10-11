import pandas as pd # pragma: no cover
import sys # pragma: no cover

data = {'foo': {'bar': 0, 'baz': {'qux': 1}}} # pragma: no cover
key_string = '' # pragma: no cover
separator = '.' # pragma: no cover
normalized_dict = {} # pragma: no cover
_normalise_json = lambda data, key_string, normalized_dict, separator: None # pragma: no cover

import pandas as pd # pragma: no cover
import sys # pragma: no cover

data = {'foo': {'bar': 0, 'baz': {'qux': 1}}, 'hello': 'world'} # pragma: no cover
key_string = '' # pragma: no cover
separator = '.' # pragma: no cover
normalized_dict = {} # pragma: no cover
_normalise_json = lambda data, key_string, normalized_dict, separator: normalized_dict.update({key_string: data}) if not isinstance(data, dict) else ({'key_string': key_string, 'separator': separator}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/json/_normalize.py
from l3.Runtime import _l_
"""
    Main recursive function
    Designed for the most basic use case of pd.json_normalize(data)
    intended as a performance improvement, see #15621

    Parameters
    ----------
    data : Any
        Type dependent on types contained within nested Json
    key_string : str
        New key (with separator(s) in) for data
    normalized_dict : dict
        The new normalized/flattened Json dict
    separator : str, default '.'
        Nested records will generate names separated by sep,
        e.g., for sep='.', { 'foo' : { 'bar' : 0 } } -> foo.bar
    """
if isinstance(data, dict):
    _l_(10798)

    for key, value in data.items():
        _l_(10796)

        new_key = f"{key_string}{separator}{key}"
        _l_(10788)

        if not key_string:
            _l_(10794)

            if sys.version_info < (3, 9):
                _l_(10793)

                try:
                    from pandas.util._str_methods import removeprefix
                    _l_(10790)

                except ImportError:
                    pass

                new_key = removeprefix(new_key, separator)
                _l_(10791)
            else:
                new_key = new_key.removeprefix(separator)
                _l_(10792)

        _normalise_json(
            data=value,
            key_string=new_key,
            normalized_dict=normalized_dict,
            separator=separator,
        )
        _l_(10795)
else:
    normalized_dict[key_string] = data
    _l_(10797)
aux = normalized_dict
_l_(10799)
exit(aux)
