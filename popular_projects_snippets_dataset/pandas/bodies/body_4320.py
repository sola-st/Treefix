# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
index = ["A", "B", "C"]
columns = ["X", "Y", "Z"]
df = DataFrame(np.random.randn(3, 3), index=index, columns=columns)

align = pd.core.ops.align_method_FRAME
# length mismatch
msg = "Unable to coerce to Series, length must be 3: given 2"
with pytest.raises(ValueError, match=msg):
    align(df, val, "index")

with pytest.raises(ValueError, match=msg):
    align(df, val, "columns")
