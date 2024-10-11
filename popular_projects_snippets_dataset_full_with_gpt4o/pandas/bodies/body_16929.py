# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
df = DataFrame(
    {
        "bools": np.random.randn(10) > 0,
        "ints": np.random.randint(0, 10, 10),
        "floats": np.random.randn(10),
        "strings": ["foo", "bar"] * 5,
    }
)

a = df[:5].loc[:, ["bools", "ints", "floats"]]
b = df[5:].loc[:, ["strings", "ints", "floats"]]

appended = a._append(b, sort=sort)
assert isna(appended["strings"][0:4]).all()
assert isna(appended["bools"][5:]).all()
