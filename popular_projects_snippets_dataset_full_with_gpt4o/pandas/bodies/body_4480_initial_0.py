import numpy as np # pragma: no cover
from pandas import DataFrame, Timestamp, Series # pragma: no cover
from datetime import datetime # pragma: no cover
import pandas._testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
from l3.Runtime import _l_
intname = np.dtype(np.int_).name
_l_(21669)
floatname = np.dtype(np.float_).name
_l_(21670)
datetime64name = np.dtype("M8[ns]").name
_l_(21671)
objectname = np.dtype(np.object_).name
_l_(21672)

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
_l_(21673)
result = df.dtypes
_l_(21674)
expected = Series(
    [np.dtype("int64")]
    + [np.dtype(objectname)] * 2
    + [np.dtype(datetime64name)] * 2,
    index=list("ABCDE"),
)
_l_(21675)
tm.assert_series_equal(result, expected)
_l_(21676)

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
_l_(21677)
result = df.dtypes
_l_(21678)
expected = Series(
    [np.dtype("float64")]
    + [np.dtype("int64")]
    + [np.dtype("object")]
    + [np.dtype("float64")]
    + [np.dtype(intname)],
    index=["a", "b", "c", floatname, intname],
)
_l_(21679)
tm.assert_series_equal(result, expected)
_l_(21680)

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
_l_(21681)
result = df.dtypes
_l_(21682)
expected = Series(
    [np.dtype("float64")]
    + [np.dtype("int64")]
    + [np.dtype("object")]
    + [np.dtype("float64")]
    + [np.dtype(intname)],
    index=["a", "b", "c", floatname, intname],
)
_l_(21683)
tm.assert_series_equal(result, expected)
_l_(21684)
