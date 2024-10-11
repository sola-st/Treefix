# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_explode.py
# https://github.com/pandas-dev/pandas/issues/35614
df = pd.DataFrame({"a": [{"x", "y"}], "b": [1]}, index=[1])
result = df.explode(column="a").sort_values(by="a")
expected = pd.DataFrame({"a": ["x", "y"], "b": [1, 1]}, index=[1, 1])
tm.assert_frame_equal(result, expected)
