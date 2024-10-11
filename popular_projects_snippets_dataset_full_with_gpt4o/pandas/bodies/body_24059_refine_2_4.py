import sys # pragma: no cover
from typing import Any, Dict # pragma: no cover

data: Any = {'foo': {'bar': 0}} # pragma: no cover
key_string: str = '' # pragma: no cover
separator: str = '.' # pragma: no cover
normalized_dict: Dict[str, Any] = {} # pragma: no cover
sys = type('Mock', (object,), {'version_info': (3, 9)}) # pragma: no cover
def _normalise_json(data: Any, key_string: str, normalized_dict: Dict[str, Any], separator: str = '.'):# pragma: no cover
    if isinstance(data, dict):# pragma: no cover
        for key, value in data.items():# pragma: no cover
            new_key = f"{key_string}{separator}{key}"# pragma: no cover
            if not key_string:# pragma: no cover
                if sys.version_info < (3, 9):# pragma: no cover
                    new_key = removeprefix(new_key, separator)# pragma: no cover
                else:# pragma: no cover
                    new_key = new_key.removeprefix(separator)# pragma: no cover
            _normalise_json(data=value, key_string=new_key, normalized_dict=normalized_dict, separator=separator)# pragma: no cover
    else:# pragma: no cover
        normalized_dict[key_string] = data# pragma: no cover
    return normalized_dict # pragma: no cover

import sys # pragma: no cover
from typing import Any, Dict # pragma: no cover

data: Any = {'foo': {'bar': 0}} # pragma: no cover
key_string: str = '' # pragma: no cover
separator: str = '.' # pragma: no cover
normalized_dict: Dict[str, Any] = {} # pragma: no cover
sys = type('Mock', (object,), {'version_info': (3, 8)}) # pragma: no cover
def _normalise_json(data: Any, key_string: str, normalized_dict: Dict[str, Any], separator: str = '.'):# pragma: no cover
    if isinstance(data, dict):# pragma: no cover
        for key, value in data.items():# pragma: no cover
            new_key = f"{key_string}{separator}{key}"# pragma: no cover
            if not key_string:# pragma: no cover
                new_key = new_key[len(separator):]# pragma: no cover
            _normalise_json(data=value, key_string=new_key, normalized_dict=normalized_dict, separator=separator)# pragma: no cover
    else:# pragma: no cover
        normalized_dict[key_string] = data# pragma: no cover
    return normalized_dict # pragma: no cover

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
    _l_(22374)

    for key, value in data.items():
        _l_(22372)

        new_key = f"{key_string}{separator}{key}"
        _l_(22364)

        if not key_string:
            _l_(22370)

            if sys.version_info < (3, 9):
                _l_(22369)

                try:
                    from pandas.util._str_methods import removeprefix
                    _l_(22366)

                except ImportError:
                    pass

                new_key = removeprefix(new_key, separator)
                _l_(22367)
            else:
                new_key = new_key.removeprefix(separator)
                _l_(22368)

        _normalise_json(
            data=value,
            key_string=new_key,
            normalized_dict=normalized_dict,
            separator=separator,
        )
        _l_(22371)
else:
    normalized_dict[key_string] = data
    _l_(22373)
aux = normalized_dict
_l_(22375)
exit(aux)
