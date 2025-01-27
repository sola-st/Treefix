# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py
# GH#46904
df = DataFrame({"a": [1, 1, 2], "b": [3, 4, 5], "c": [6, 7, 8]})
r = df.rolling(window=3, axis=1)
with pytest.raises(NotImplementedError, match="axis other than 0 is not supported"):
    r.agg(func)
