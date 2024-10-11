# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
# GH#4763
df = DataFrame(
    {
        "vals": [1, 2, 3, 4],
        "ids": ["a", "b", "f", "n"],
        "ids2": ["a", "n", "c", "n"],
    },
    index=["foo", "bar", "baz", "qux"],
)
msg = (
    r"only list-like or dict-like objects are allowed "
    r"to be passed to DataFrame.isin\(\), you passed a 'str'"
)
with pytest.raises(TypeError, match=msg):
    df.isin("a")

with pytest.raises(TypeError, match=msg):
    df.isin("aaa")
