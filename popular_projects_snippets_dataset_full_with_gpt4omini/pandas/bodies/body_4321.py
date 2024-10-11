# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
index = ["A", "B", "C"]
columns = ["X", "Y", "Z"]
df = DataFrame(np.random.randn(3, 3), index=index, columns=columns)

align = pd.core.ops.align_method_FRAME
val = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tm.assert_frame_equal(
    align(df, val, "index")[1],
    DataFrame(val, index=df.index, columns=df.columns),
)
tm.assert_frame_equal(
    align(df, val, "columns")[1],
    DataFrame(val, index=df.index, columns=df.columns),
)

# shape mismatch
msg = "Unable to coerce to DataFrame, shape must be"
val = np.array([[1, 2, 3], [4, 5, 6]])
with pytest.raises(ValueError, match=msg):
    align(df, val, "index")

with pytest.raises(ValueError, match=msg):
    align(df, val, "columns")

val = np.zeros((3, 3, 3))
msg = re.escape(
    "Unable to coerce to Series/DataFrame, dimension must be <= 2: (3, 3, 3)"
)
with pytest.raises(ValueError, match=msg):
    align(df, val, "index")
with pytest.raises(ValueError, match=msg):
    align(df, val, "columns")
