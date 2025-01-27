# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH 13912
df = DataFrame({"a": [1], "b": [1.1], "c": ["foo"], "d": [ts_value]})
with pytest.raises(TypeError, match="does not support reduction"):
    df.sum()
