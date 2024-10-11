# Extracted from ./data/repos/pandas/pandas/tests/frame/test_alter_axes.py
float_frame["hi"] = "there"

df = float_frame.copy()
df.columns = ["foo", "bar", "baz", "quux", "foo2"]
tm.assert_series_equal(float_frame["C"], df["baz"], check_names=False)
tm.assert_series_equal(float_frame["hi"], df["foo2"], check_names=False)
