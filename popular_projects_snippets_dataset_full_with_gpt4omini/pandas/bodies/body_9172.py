# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py

# Codes should be read only
c = Categorical(["a", "b", "c", "a", np.nan])
exp = np.array([0, 1, 2, 0, -1], dtype="int8")
tm.assert_numpy_array_equal(c.codes, exp)

# Assignments to codes should raise
msg = (
    "property 'codes' of 'Categorical' object has no setter"
    if PY311
    else "can't set attribute"
)
with pytest.raises(AttributeError, match=msg):
    c.codes = np.array([0, 1, 2, 0, 1], dtype="int8")

# changes in the codes array should raise
codes = c.codes

with pytest.raises(ValueError, match="assignment destination is read-only"):
    codes[4] = 1

# But even after getting the codes, the original array should still be
# writeable!
c[4] = "a"
exp = np.array([0, 1, 2, 0, 0], dtype="int8")
tm.assert_numpy_array_equal(c.codes, exp)
c._codes[4] = 2
exp = np.array([0, 1, 2, 0, 2], dtype="int8")
tm.assert_numpy_array_equal(c.codes, exp)
