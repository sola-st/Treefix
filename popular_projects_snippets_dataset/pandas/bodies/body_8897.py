# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
import pyarrow as pa

from pandas.core.arrays.arrow.extension_types import ArrowIntervalType

intervals = pd.interval_range(1, 5, freq=1).array

result = pa.array(intervals)
assert isinstance(result.type, ArrowIntervalType)
assert result.type.closed == intervals.closed
assert result.type.subtype == pa.int64()
assert result.storage.field("left").equals(pa.array([1, 2, 3, 4], type="int64"))
assert result.storage.field("right").equals(pa.array([2, 3, 4, 5], type="int64"))

expected = pa.array([{"left": i, "right": i + 1} for i in range(1, 5)])
assert result.storage.equals(expected)

# convert to its storage type
result = pa.array(intervals, type=expected.type)
assert result.equals(expected)

# unsupported conversions
with pytest.raises(TypeError, match="Not supported to convert IntervalArray"):
    pa.array(intervals, type="float64")

with pytest.raises(TypeError, match="Not supported to convert IntervalArray"):
    pa.array(intervals, type=ArrowIntervalType(pa.float64(), "left"))
