import numpy as np # pragma: no cover
from numpy import issubdtype # pragma: no cover
from numpy import integer, bool_, object_ # pragma: no cover
import numbers # pragma: no cover

x = np.array([1, 2, 3], dtype=object) # pragma: no cover
is_integer_dtype = lambda dtype: issubdtype(dtype, integer) # pragma: no cover
is_bool_dtype = lambda dtype: issubdtype(dtype, bool_) # pragma: no cover
is_object_dtype = lambda dtype: issubdtype(dtype, object_) # pragma: no cover
is_float = lambda x: isinstance(x, float) # pragma: no cover
is_integer = lambda x: isinstance(x, int) # pragma: no cover
is_complex = lambda x: isinstance(x, complex) # pragma: no cover

import numpy as np # pragma: no cover
from pandas.api.types import is_integer_dtype, is_bool_dtype, is_object_dtype # pragma: no cover

x = np.array([1, 2, 3, 'foo'], dtype=object) # pragma: no cover
is_integer_dtype = lambda arr: np.issubdtype(arr.dtype, np.integer) # pragma: no cover
is_bool_dtype = lambda arr: np.issubdtype(arr.dtype, np.bool_) # pragma: no cover
is_object_dtype = lambda arr: np.issubdtype(arr.dtype, np.object_) # pragma: no cover
is_float = lambda x: isinstance(x, float) # pragma: no cover
is_integer = lambda x: isinstance(x, int) # pragma: no cover
is_complex = lambda x: isinstance(x, complex) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/nanops.py
from l3.Runtime import _l_
if isinstance(x, np.ndarray):
    _l_(19732)

    if is_integer_dtype(x) or is_bool_dtype(x):
        _l_(19723)

        x = x.astype(np.float64)
        _l_(19712)
    elif is_object_dtype(x):
        _l_(19722)

        try:
            _l_(19721)

            x = x.astype(np.complex128)
            _l_(19713)
        except (TypeError, ValueError):
            _l_(19718)

            try:
                _l_(19717)

                x = x.astype(np.float64)
                _l_(19714)
            except ValueError as err:
                _l_(19716)

                # GH#29941 we get here with object arrays containing strs
                raise TypeError(f"Could not convert {x} to numeric") from err
                _l_(19715)
        else:
            if not np.any(np.imag(x)):
                _l_(19720)

                x = x.real
                _l_(19719)
elif not (is_float(x) or is_integer(x) or is_complex(x)):
    _l_(19731)

    try:
        _l_(19730)

        x = float(x)
        _l_(19724)
    except (TypeError, ValueError):
        _l_(19729)

        # e.g. "1+1j" or "foo"
        try:
            _l_(19728)

            x = complex(x)
            _l_(19725)
        except ValueError as err:
            _l_(19727)

            # e.g. "foo"
            raise TypeError(f"Could not convert {x} to numeric") from err
            _l_(19726)
aux = x
_l_(19733)
exit(aux)
