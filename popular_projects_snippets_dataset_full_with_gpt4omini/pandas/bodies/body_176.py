# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
from pandas.tseries.offsets import BDay

df = DataFrame({"x1": [datetime(1996, 1, 1)]})

df = df.applymap(lambda x: x + BDay())
df = df.applymap(lambda x: x + BDay())

result = df.x1.dtype
assert result == "M8[ns]"
