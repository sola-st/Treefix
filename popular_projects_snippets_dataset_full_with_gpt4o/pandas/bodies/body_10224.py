# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_raises.py
df = DataFrame(
    {
        "a": [1, 1, 1, 2, 2],
        "b": range(5),
        "c": list("xyzwt"),
    }
)
gb = df.groupby("a")

def func(x):
    raise TypeError("Test error message")

with pytest.raises(TypeError, match="Test error message"):
    getattr(gb, how)(func)
