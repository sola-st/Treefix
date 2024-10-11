# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
lhs = Series(np.array(list("abc"), "S1").astype(object))
rhs = Series(np.array(list("def"), "S1").astype(object))
msg = "Cannot use .str.cat with values of inferred dtype 'bytes'"
with pytest.raises(TypeError, match=msg):
    lhs.str.cat(rhs)
