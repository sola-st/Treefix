# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 12213
data = '["a", NaN, "NaN", Infinity, "Infinity", -Infinity, "-Infinity"]'
result = read_json(data)
expected = DataFrame(
    ["a", np.nan, "NaN", np.inf, "Infinity", -np.inf, "-Infinity"]
)
tm.assert_frame_equal(result, expected)
