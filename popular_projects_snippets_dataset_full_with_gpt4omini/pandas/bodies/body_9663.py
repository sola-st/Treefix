# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_arrow_compat.py
from pandas.core.arrays.arrow.extension_types import ArrowPeriodType

arr = PeriodArray([1, 2, 3], freq="D")
arr[1] = pd.NaT

result = pa.array(arr)
assert isinstance(result.type, ArrowPeriodType)
assert result.type.freq == "D"
expected = pa.array([1, None, 3], type="int64")
assert result.storage.equals(expected)
