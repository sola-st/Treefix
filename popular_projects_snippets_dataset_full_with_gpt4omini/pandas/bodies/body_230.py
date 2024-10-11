# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 16832
if method == "sum":
    msg = r'can only concatenate str \(not "int"\) to str'
else:
    msg = "not supported between instances of 'str' and 'float'"
with pytest.raises(TypeError, match=msg):
    getattr(df, method)()
