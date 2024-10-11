import numpy as np # pragma: no cover
from numpy import float64 as np_float64 # pragma: no cover
from numpy import complex128 as np_complex128 # pragma: no cover

x = np.array([1, 2, 3]) # pragma: no cover
np.ndarray = type('MockNdarray', (object,), {}) # pragma: no cover
np.float64 = np_float64 # pragma: no cover
np.complex128 = np_complex128 # pragma: no cover
np.any = np.any # pragma: no cover
np.imag = lambda array: array * 0j # pragma: no cover
x.real = x.tolist() # pragma: no cover

import numpy as np # pragma: no cover

x = np.array([1, 2, 3], dtype=int) # pragma: no cover
np.ndarray = type('MockNdarray', (object,), {'astype': lambda self, dtype: np.array([1.0, 2.0, 3.0], dtype=dtype), 'tolist': lambda self: [1.0, 2.0, 3.0]}) # pragma: no cover
np.float64 = np.dtype('float64') # pragma: no cover
np.complex128 = np.dtype('complex128') # pragma: no cover
np.any = lambda arr: arr.size > 0 # pragma: no cover
np.imag = lambda arr: np.zeros(arr.shape) # pragma: no cover
x.real = x # pragma: no cover
is_float = lambda val: np.issubdtype(type(val), np.float64) # pragma: no cover
is_integer = lambda val: np.issubdtype(type(val), np.integer) # pragma: no cover
is_complex = lambda val: np.issubdtype(type(val), np.complex_) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/nanops.py
from l3.Runtime import _l_
if isinstance(x, np.ndarray):
    _l_(9421)

    if is_integer_dtype(x) or is_bool_dtype(x):
        _l_(9412)

        x = x.astype(np.float64)
        _l_(9401)
    elif is_object_dtype(x):
        _l_(9411)

        try:
            _l_(9410)

            x = x.astype(np.complex128)
            _l_(9402)
        except (TypeError, ValueError):
            _l_(9407)

            try:
                _l_(9406)

                x = x.astype(np.float64)
                _l_(9403)
            except ValueError as err:
                _l_(9405)

                # GH#29941 we get here with object arrays containing strs
                raise TypeError(f"Could not convert {x} to numeric") from err
                _l_(9404)
        else:
            if not np.any(np.imag(x)):
                _l_(9409)

                x = x.real
                _l_(9408)
elif not (is_float(x) or is_integer(x) or is_complex(x)):
    _l_(9420)

    try:
        _l_(9419)

        x = float(x)
        _l_(9413)
    except (TypeError, ValueError):
        _l_(9418)

        # e.g. "1+1j" or "foo"
        try:
            _l_(9417)

            x = complex(x)
            _l_(9414)
        except ValueError as err:
            _l_(9416)

            # e.g. "foo"
            raise TypeError(f"Could not convert {x} to numeric") from err
            _l_(9415)
aux = x
_l_(9422)
exit(aux)
