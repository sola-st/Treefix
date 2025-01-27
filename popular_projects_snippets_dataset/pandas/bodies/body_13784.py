# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
df = DataFrame({"A": [0, 1]})
result = (
    df.style.set_properties(subset=IndexSlice[0, "A"], color="white")
    ._compute()
    .ctx
)
expected = {(0, 0): [("color", "white")]}
assert result == expected
