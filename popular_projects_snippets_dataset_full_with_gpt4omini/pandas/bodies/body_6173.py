# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
data = data[:5]
if is_bool_dtype(data.dtype):
    op = operator.xor
else:
    op = operator.sub
try:
    # does this array implement ops?
    op(data, data)
except Exception:
    pytest.skip(f"{type(data)} does not support diff")
s = pd.Series(data)
result = s.diff(periods)
expected = pd.Series(op(data, data.shift(periods)))
self.assert_series_equal(result, expected)

df = pd.DataFrame({"A": data, "B": [1.0] * 5})
result = df.diff(periods)
if periods == 1:
    b = [np.nan, 0, 0, 0, 0]
else:
    b = [0, 0, 0, np.nan, np.nan]
expected = pd.DataFrame({"A": expected, "B": b})
self.assert_frame_equal(result, expected)
