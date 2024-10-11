import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pytest # pragma: no cover

kernel = 'nunique' # pragma: no cover
keys = 'a1' # pragma: no cover
has_arg = True # pragma: no cover
df = DataFrame({'a1': [1, 1], 'a2': [2, 2], 'a3': [5, 6], 'b': [object(), object()]}) # pragma: no cover
def get_groupby_method_args(kernel, df): return [], {} # pragma: no cover
args = get_groupby_method_args(kernel, df) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH#46072
# drops_nuisance: Whether the op drops nuisance columns even when numeric_only=False
# has_arg: Whether the op has a numeric_only arg
from l3.Runtime import _l_
df = DataFrame({"a1": [1, 1], "a2": [2, 2], "a3": [5, 6], "b": 2 * [object]})
_l_(8340)

args = get_groupby_method_args(kernel, df)
_l_(8341)
kwargs = {} if numeric_only is lib.no_default else {"numeric_only": numeric_only}
_l_(8342)

gb = df.groupby(keys)
_l_(8343)
method = getattr(gb, kernel)
_l_(8344)
if has_arg and numeric_only is True:
    _l_(8363)

    # Cases where b does not appear in the result
    result = method(*args, **kwargs)
    _l_(8345)
    assert "b" not in result.columns
    _l_(8346)
elif (
    # kernels that work on any dtype and have numeric_only arg
    kernel in ("first", "last")
    or (
        # kernels that work on any dtype and don't have numeric_only arg
        kernel in ("any", "all", "bfill", "ffill", "fillna", "nth", "nunique")
        and numeric_only is lib.no_default
    )
):
    _l_(8362)

    result = method(*args, **kwargs)
    _l_(8347)
    assert "b" in result.columns
    _l_(8348)
elif has_arg or kernel in ("idxmax", "idxmin"):
    _l_(8361)

    assert numeric_only is not True
    _l_(8349)
    # kernels that are successful on any dtype were above; this will fail

    # object dtypes for transformations are not implemented in Cython and
    # have no Python fallback
    exception = NotImplementedError if kernel.startswith("cum") else TypeError
    _l_(8350)

    msg = "|".join(
        [
            "not allowed for this dtype",
            "must be a string or a number",
            "cannot be performed against 'object' dtypes",
            "must be a string or a real number",
            "unsupported operand type",
            "not supported between instances of",
            "function is not implemented for this dtype",
        ]
    )
    _l_(8351)
    with pytest.raises(exception, match=msg):
        _l_(8353)

        method(*args, **kwargs)
        _l_(8352)
elif not has_arg and numeric_only is not lib.no_default:
    _l_(8360)

    with pytest.raises(
        TypeError, match="got an unexpected keyword argument 'numeric_only'"
    ):
        _l_(8355)

        method(*args, **kwargs)
        _l_(8354)
else:
    assert kernel in ("diff", "pct_change")
    _l_(8356)
    assert numeric_only is lib.no_default
    _l_(8357)
    # Doesn't have numeric_only argument and fails on nuisance columns
    with pytest.raises(TypeError, match=r"unsupported operand type"):
        _l_(8359)

        method(*args, **kwargs)
        _l_(8358)
