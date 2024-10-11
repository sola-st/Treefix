import numpy as np # pragma: no cover
import pandas._testing as tm # pragma: no cover

res = type('Mock', (object,), {'asm8': np.array([1, 2, 3]), 'shape': (3,), 'dtype': type('Mock', (object,), {'kind': 'O'})}) # pragma: no cover
axis = 1 # pragma: no cover
targ = type('Mock', (object,), {'shape': (2,), 'dtype': type('Mock', (object,), {'kind': 'O', 'name': 'O'}), 'ndim': True}) # pragma: no cover
check_dtype = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
from l3.Runtime import _l_
res = getattr(res, "asm8", res)
_l_(15464)

if (
    axis != 0
    and hasattr(targ, "shape")
    and targ.ndim
    and targ.shape != res.shape
):
    _l_(15466)

    res = np.split(res, [targ.shape[0]], axis=0)[0]
    _l_(15465)

try:
    _l_(15483)

    tm.assert_almost_equal(targ, res, check_dtype=check_dtype)
    _l_(15467)
except AssertionError:
    _l_(15482)


    # handle timedelta dtypes
    if hasattr(targ, "dtype") and targ.dtype == "m8[ns]":
        _l_(15469)

        raise
        _l_(15468)

    # There are sometimes rounding errors with
    # complex and object dtypes.
    # If it isn't one of those, re-raise the error.
    if not hasattr(res, "dtype") or res.dtype.kind not in ["c", "O"]:
        _l_(15471)

        raise
        _l_(15470)
    # convert object dtypes to something that can be split into
    # real and imaginary parts
    if res.dtype.kind == "O":
        _l_(15479)

        if targ.dtype.kind != "O":
            _l_(15476)

            res = res.astype(targ.dtype)
            _l_(15472)
        else:
            cast_dtype = "c16" if hasattr(np, "complex128") else "f8"
            _l_(15473)
            res = res.astype(cast_dtype)
            _l_(15474)
            targ = targ.astype(cast_dtype)
            _l_(15475)
            # there should never be a case where numpy returns an object
            # but nanops doesn't, so make that an exception
    elif targ.dtype.kind == "O":
        _l_(15478)

        raise
        _l_(15477)
    tm.assert_almost_equal(np.real(targ), np.real(res), check_dtype=check_dtype)
    _l_(15480)
    tm.assert_almost_equal(np.imag(targ), np.imag(res), check_dtype=check_dtype)
    _l_(15481)
