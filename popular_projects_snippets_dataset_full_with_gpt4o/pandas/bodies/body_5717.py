# Extracted from ./data/repos/pandas/pandas/tests/extension/test_period.py
# Override to use __sub__ instead of __add__
other = pd.Series(data)
if frame_or_series is pd.DataFrame:
    other = other.to_frame()

result = data.__sub__(other)
assert result is NotImplemented
