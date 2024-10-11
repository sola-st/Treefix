# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#16927: When converting to a dict, if a column has a non-unique name
# it will be dropped, throwing a warning.
df = DataFrame([[1, 2, 3]], columns=["a", "a", "b"])
with tm.assert_produces_warning(UserWarning):
    df.to_dict()
