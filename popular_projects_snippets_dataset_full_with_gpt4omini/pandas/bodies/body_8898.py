# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
import pyarrow as pa

from pandas.core.arrays.arrow.extension_types import ArrowIntervalType

arr = IntervalArray.from_breaks([0.0, 1.0, 2.0, 3.0])
arr[1] = None

result = pa.array(arr)
assert isinstance(result.type, ArrowIntervalType)
assert result.type.closed == arr.closed
assert result.type.subtype == pa.float64()

# fields have missing values (not NaN)
left = pa.array([0.0, None, 2.0], type="float64")
right = pa.array([1.0, None, 3.0], type="float64")
assert result.storage.field("left").equals(left)
assert result.storage.field("right").equals(right)

# structarray itself also has missing values on the array level
vals = [
    {"left": 0.0, "right": 1.0},
    {"left": None, "right": None},
    {"left": 2.0, "right": 3.0},
]
expected = pa.StructArray.from_pandas(vals, mask=np.array([False, True, False]))
assert result.storage.equals(expected)
