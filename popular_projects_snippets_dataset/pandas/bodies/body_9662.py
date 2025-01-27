# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_arrow_compat.py
from pandas.core.arrays.arrow.extension_types import ArrowPeriodType

periods = period_array(data, freq=freq)
result = pa.array(periods)
assert isinstance(result.type, ArrowPeriodType)
assert result.type.freq == freq
expected = pa.array(periods.asi8, type="int64")
assert result.storage.equals(expected)

# convert to its storage type
result = pa.array(periods, type=pa.int64())
assert result.equals(expected)

# unsupported conversions
msg = "Not supported to convert PeriodArray to 'double' type"
with pytest.raises(TypeError, match=msg):
    pa.array(periods, type="float64")

with pytest.raises(TypeError, match="different 'freq'"):
    pa.array(periods, type=ArrowPeriodType("T"))
