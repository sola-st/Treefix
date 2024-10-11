# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
df = DataFrame({"a": list("abc"), "b": list(range(1, 4))})
msg = "at least one of include or exclude must be nonempty"
with pytest.raises(ValueError, match=msg):
    df.select_dtypes()
