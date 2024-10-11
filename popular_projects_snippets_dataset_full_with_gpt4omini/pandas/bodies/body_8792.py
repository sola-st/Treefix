# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if dtype.storage == "pyarrow":
    reason = "Failed: DID NOT RAISE <class 'ValueError'>"
    mark = pytest.mark.xfail(raises=None, reason=reason)
    request.node.add_marker(mark)

a = pd.array(["a", "b", "c"], dtype=dtype)
b = np.array([["a", "b", "c"]], dtype=object)
with pytest.raises(ValueError, match="3 != 1"):
    a + b

s = pd.Series(a)
with pytest.raises(ValueError, match="3 != 1"):
    s + b
