# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
obj = pd.Series(["a", "b", "c "])
if frame:
    obj = obj.to_frame()

msg = "'to_replace' must be 'None' if 'regex' is not a bool"
with pytest.raises(ValueError, match=msg):
    obj.replace(to_replace=["a"], regex="foo")
