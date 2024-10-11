import numpy as np # pragma: no cover
from numpy import isfinite as is_float # pragma: no cover
from numpy import iscomplex as is_complex # pragma: no cover

x = np.array([1, 2, 3]) # pragma: no cover
np = type('Mock', (object,), {'ndarray': np.ndarray, 'float64': np.float64, 'complex128': np.complex128, 'any': np.any, 'imag': lambda a: a.imag})() # pragma: no cover
is_integer_dtype = lambda arr: np.issubdtype(arr.dtype, np.integer) # pragma: no cover
is_bool_dtype = lambda arr: np.issubdtype(arr.dtype, np.bool_) # pragma: no cover
is_object_dtype = lambda arr: np.issubdtype(arr.dtype, np.object_) # pragma: no cover
is_float = lambda val: isinstance(val, float) # pragma: no cover
is_integer = lambda val: isinstance(val, int) # pragma: no cover
is_complex = lambda val: isinstance(val, complex) # pragma: no cover

import numpy as np # pragma: no cover
from numpy import iscomplex as is_complex # pragma: no cover

x = np.array([1, 2, 3], dtype=int) # pragma: no cover
class MockNDArray(np.ndarray): pass # pragma: no cover
np.ndarray = MockNDArray # pragma: no cover
np.float64 = np.dtype('float64') # pragma: no cover
np.complex128 = np.dtype('complex128') # pragma: no cover
np.any = lambda arr: arr.size > 0 # pragma: no cover
np.imag = lambda arr: np.zeros_like(arr) # pragma: no cover
x.real = x # pragma: no cover
np.issubdtype = np.issubdtype # pragma: no cover

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
