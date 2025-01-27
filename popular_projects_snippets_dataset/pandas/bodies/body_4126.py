# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#46852
df = DataFrame({"a": [1, 2, 3], "b": object})
args = (df,) if kernel == "corrwith" else ()
msg = "|".join(
    [
        "not allowed for this dtype",
        "argument must be a string or a number",
        "not supported between instances of",
        "unsupported operand type",
        "argument must be a string or a real number",
    ]
)
with pytest.raises(TypeError, match=msg):
    getattr(df, kernel)(*args)
