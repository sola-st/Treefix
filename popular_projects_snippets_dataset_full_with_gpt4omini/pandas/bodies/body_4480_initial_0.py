import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover
from datetime import datetime # pragma: no cover
from pandas import Series # pragma: no cover

np = type('Mock', (object,), {'dtype': np.dtype, 'int_': np.int_, 'float_': np.float_, 'object_': np.object_, 'arange': np.arange, 'array': np.array})() # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
Timestamp = Timestamp # pragma: no cover
datetime = datetime # pragma: no cover
Series = Series # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': lambda x, y: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
from l3.Runtime import _l_
intname = np.dtype(np.int_).name
_l_(10497)
floatname = np.dtype(np.float_).name
_l_(10498)
datetime64name = np.dtype("M8[ns]").name
_l_(10499)
objectname = np.dtype(np.object_).name
_l_(10500)

# single item
df = DataFrame(
    {
        "A": 1,
        "B": "foo",
        "C": "bar",
        "D": Timestamp("20010101"),
        "E": datetime(2001, 1, 2, 0, 0),
    },
    index=np.arange(10),
)
_l_(10501)
result = df.dtypes
_l_(10502)
expected = Series(
    [np.dtype("int64")]
    + [np.dtype(objectname)] * 2
    + [np.dtype(datetime64name)] * 2,
    index=list("ABCDE"),
)
_l_(10503)
tm.assert_series_equal(result, expected)
_l_(10504)

# check with ndarray construction ndim==0 (e.g. we are passing a ndim 0
# ndarray with a dtype specified)
df = DataFrame(
    {
        "a": 1.0,
        "b": 2,
        "c": "foo",
        floatname: np.array(1.0, dtype=floatname),
        intname: np.array(1, dtype=intname),
    },
    index=np.arange(10),
)
_l_(10505)
result = df.dtypes
_l_(10506)
expected = Series(
    [np.dtype("float64")]
    + [np.dtype("int64")]
    + [np.dtype("object")]
    + [np.dtype("float64")]
    + [np.dtype(intname)],
    index=["a", "b", "c", floatname, intname],
)
_l_(10507)
tm.assert_series_equal(result, expected)
_l_(10508)

# check with ndarray construction ndim>0
df = DataFrame(
    {
        "a": 1.0,
        "b": 2,
        "c": "foo",
        floatname: np.array([1.0] * 10, dtype=floatname),
        intname: np.array([1] * 10, dtype=intname),
    },
    index=np.arange(10),
)
_l_(10509)
result = df.dtypes
_l_(10510)
expected = Series(
    [np.dtype("float64")]
    + [np.dtype("int64")]
    + [np.dtype("object")]
    + [np.dtype("float64")]
    + [np.dtype(intname)],
    index=["a", "b", "c", floatname, intname],
)
_l_(10511)
tm.assert_series_equal(result, expected)
_l_(10512)
