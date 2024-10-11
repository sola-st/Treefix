# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#48293
df = DataFrame({"a": [1], "b": 1})
with pytest.raises(TypeError, match="missing 1 required argument"):
    df.pivot()
