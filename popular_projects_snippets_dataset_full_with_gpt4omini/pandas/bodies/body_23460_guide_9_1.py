import numpy as np # pragma: no cover
from pandas.api.types import is_integer_dtype, is_bool_dtype, is_object_dtype, is_float, is_integer, is_complex # pragma: no cover

x = np.array(['1', '2', 'invalid']) # pragma: no cover

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
