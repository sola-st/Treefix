import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import testing as tm # pragma: no cover

res = np.array([[1, 2], [3, 4]], dtype=np.float64) # pragma: no cover
axis = 0 # pragma: no cover
targ = np.array([[1, 2], [3, 4]], dtype=np.float64) # pragma: no cover
check_dtype = True # pragma: no cover

import numpy as np # pragma: no cover
import numpy.testing as tm # pragma: no cover

res = np.array([[1, 2], [3, 4]], dtype=np.float64) # pragma: no cover
axis = 0 # pragma: no cover
targ = np.array([[1, 2], [3, 4]], dtype=np.float64) # pragma: no cover
check_dtype = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
from l3.Runtime import _l_
res = getattr(res, "asm8", res)
_l_(3890)

if (
    axis != 0
    and hasattr(targ, "shape")
    and targ.ndim
    and targ.shape != res.shape
):
    _l_(3892)

    res = np.split(res, [targ.shape[0]], axis=0)[0]
    _l_(3891)

try:
    _l_(3909)

    tm.assert_almost_equal(targ, res, check_dtype=check_dtype)
    _l_(3893)
except AssertionError:
    _l_(3908)


    # handle timedelta dtypes
    if hasattr(targ, "dtype") and targ.dtype == "m8[ns]":
        _l_(3895)

        raise
        _l_(3894)

    # There are sometimes rounding errors with
    # complex and object dtypes.
    # If it isn't one of those, re-raise the error.
    if not hasattr(res, "dtype") or res.dtype.kind not in ["c", "O"]:
        _l_(3897)

        raise
        _l_(3896)
    # convert object dtypes to something that can be split into
    # real and imaginary parts
    if res.dtype.kind == "O":
        _l_(3905)

        if targ.dtype.kind != "O":
            _l_(3902)

            res = res.astype(targ.dtype)
            _l_(3898)
        else:
            cast_dtype = "c16" if hasattr(np, "complex128") else "f8"
            _l_(3899)
            res = res.astype(cast_dtype)
            _l_(3900)
            targ = targ.astype(cast_dtype)
            _l_(3901)
            # there should never be a case where numpy returns an object
            # but nanops doesn't, so make that an exception
    elif targ.dtype.kind == "O":
        _l_(3904)

        raise
        _l_(3903)
    tm.assert_almost_equal(np.real(targ), np.real(res), check_dtype=check_dtype)
    _l_(3906)
    tm.assert_almost_equal(np.imag(targ), np.imag(res), check_dtype=check_dtype)
    _l_(3907)
