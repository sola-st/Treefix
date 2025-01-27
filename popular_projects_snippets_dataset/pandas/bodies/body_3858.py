# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
buf = StringIO()

# small one
repr(float_frame)
float_frame.info(verbose=False, buf=buf)

# even smaller
float_frame.reindex(columns=["A"]).info(verbose=False, buf=buf)
float_frame.reindex(columns=["A", "B"]).info(verbose=False, buf=buf)

# exhausting cases in DataFrame.info

# columns but no index
no_index = DataFrame(columns=[0, 1, 3])
repr(no_index)

# no columns or index
DataFrame().info(buf=buf)

df = DataFrame(["a\n\r\tb"], columns=["a\n\r\td"], index=["a\n\r\tf"])
assert "\t" not in repr(df)
assert "\r" not in repr(df)
assert "a\n" not in repr(df)
