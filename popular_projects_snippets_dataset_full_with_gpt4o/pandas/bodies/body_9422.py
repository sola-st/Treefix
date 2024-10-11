# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py
# some reduce ops always return float, even if the result
# is a rounded number
df = pd.DataFrame(
    {
        "A": ["a", "b", "b"],
        "B": [1, None, 3],
        "C": pd.array([1, None, 3], dtype="Int64"),
    }
)

# op
result = getattr(df.C, op)()
assert isinstance(result, float)

# groupby
result = getattr(df.groupby("A"), op)()

expected = pd.DataFrame(
    {"B": np.array([1.0, 3.0]), "C": pd.array([1, 3], dtype="Float64")},
    index=pd.Index(["a", "b"], name="A"),
)
tm.assert_frame_equal(result, expected)
