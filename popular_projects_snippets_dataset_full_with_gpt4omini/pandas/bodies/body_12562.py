# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
empty_frame = DataFrame()
data = empty_frame.to_json(orient=orient)
result = read_json(data, orient=orient, convert_axes=convert_axes)
if orient == "split":
    idx = pd.Index([], dtype=(float if convert_axes else object))
    expected = DataFrame(index=idx, columns=idx)
elif orient in ["index", "columns"]:
    # TODO: this condition is probably a bug
    idx = pd.Index([], dtype=(float if convert_axes else object))
    expected = DataFrame(columns=idx)
else:
    expected = empty_frame.copy()

tm.assert_frame_equal(result, expected)
