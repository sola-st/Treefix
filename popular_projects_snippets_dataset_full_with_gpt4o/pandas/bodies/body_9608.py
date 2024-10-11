# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
df = pd.DataFrame(
    {
        "A": ["a", "b", "b"],
        "B": [1, None, 3],
        "C": pd.array([0.1, None, 3.0], dtype="Float64"),
    }
)

# op
result = getattr(df.C, op)()
assert isinstance(result, np.float64)

# groupby
result = getattr(df.groupby("A"), op)()

expected = pd.DataFrame(
    {"B": np.array([1.0, 3.0]), "C": pd.array([0.1, 3], dtype="Float64")},
    index=pd.Index(["a", "b"], name="A"),
)
tm.assert_frame_equal(result, expected)
