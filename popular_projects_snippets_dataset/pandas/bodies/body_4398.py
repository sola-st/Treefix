# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# Test for passing dict subclass to constructor
data = {
    "col1": dict_subclass((x, 10.0 * x) for x in range(10)),
    "col2": dict_subclass((x, 20.0 * x) for x in range(10)),
}
df = DataFrame(data)
refdf = DataFrame({col: dict(val.items()) for col, val in data.items()})
tm.assert_frame_equal(refdf, df)

data = dict_subclass(data.items())
df = DataFrame(data)
tm.assert_frame_equal(refdf, df)
