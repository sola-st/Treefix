# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
# TODO(#22346): preserve Int64 dtype
# for ops that enable (mean would actually work here
# but generally it is a float return value)
df = pd.DataFrame(
    {
        "A": ["a", "b", "b"],
        "B": [1, None, 3],
        "C": pd.array([1, None, 3], dtype="Int64"),
    }
)

# op
result = getattr(df.C, op)()
if op in {"sum", "prod", "min", "max"}:
    assert isinstance(result, np.int64)
else:
    assert isinstance(result, int)

# groupby
result = getattr(df.groupby("A"), op)()

expected = pd.DataFrame(
    {"B": np.array([1.0, 3.0]), "C": pd.array([1, 3], dtype="Int64")},
    index=pd.Index(["a", "b"], name="A"),
)
tm.assert_frame_equal(result, expected)
