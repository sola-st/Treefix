# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# TODO: improve coverage with date_format parameter
data = datetime_frame.to_json(orient=orient)
result = read_json(data, orient=orient, convert_axes=convert_axes)
expected = datetime_frame.copy()

if not convert_axes:  # one off for ts handling
    # DTI gets converted to epoch values
    idx = expected.index.view(np.int64) // 1000000
    if orient != "split":  # TODO: handle consistently across orients
        idx = idx.astype(str)

    expected.index = idx

assert_json_roundtrip_equal(result, expected, orient)
