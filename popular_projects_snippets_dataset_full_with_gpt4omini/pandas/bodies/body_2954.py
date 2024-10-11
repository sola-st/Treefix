# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# GH 22985
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, dtype="object")
msg = (
    "Cannot interpolate with all object-dtype columns "
    "in the DataFrame. Try setting at least one "
    "column to a numeric dtype."
)
with pytest.raises(TypeError, match=msg):
    df.interpolate()
