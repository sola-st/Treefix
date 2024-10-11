import numpy as np # pragma: no cover
from pandas.api.extensions import ExtensionDtype # pragma: no cover
from pandas.api.types import is_hashable # pragma: no cover

dtype = type('InvalidType', (object,), {'__hash__': lambda self: None})() # pragma: no cover
registry = type('Mock', (object,), {'find': lambda self, x: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
from l3.Runtime import _l_
"""
    Convert input into a pandas only dtype object or a numpy dtype object.

    Parameters
    ----------
    dtype : object to be converted

    Returns
    -------
    np.dtype or a pandas dtype

    Raises
    ------
    TypeError if not a dtype
    """
# short-circuit
if isinstance(dtype, np.ndarray):
    _l_(22204)

    aux = dtype.dtype
    _l_(22201)
    exit(aux)
elif isinstance(dtype, (np.dtype, ExtensionDtype)):
    _l_(22203)

    aux = dtype
    _l_(22202)
    exit(aux)

# registered extension types
result = registry.find(dtype)
_l_(22205)
if result is not None:
    _l_(22207)

    aux = result
    _l_(22206)
    exit(aux)

# try a numpy dtype
# raise a consistent TypeError if failed
try:
    _l_(22211)

    npdtype = np.dtype(dtype)
    _l_(22208)
except SyntaxError as err:
    _l_(22210)

    # np.dtype uses `eval` which can raise SyntaxError
    raise TypeError(f"data type '{dtype}' not understood") from err
    _l_(22209)

# Any invalid dtype (such as pd.Timestamp) should raise an error.
# np.dtype(invalid_type).kind = 0 for such objects. However, this will
# also catch some valid dtypes such as object, np.object_ and 'object'
# which we safeguard against by catching them earlier and returning
# np.dtype(valid_dtype) before this condition is evaluated.
if is_hashable(dtype) and dtype in [object, np.object_, "object", "O"]:
    _l_(22215)

    aux = npdtype
    _l_(22212)
    # check hashability to avoid errors/DeprecationWarning when we get
    # here and `dtype` is an array
    exit(aux)
elif npdtype.kind == "O":
    _l_(22214)

    raise TypeError(f"dtype '{dtype}' not understood")
    _l_(22213)
aux = npdtype
_l_(22216)

exit(aux)
