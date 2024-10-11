# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH25468
# If metadata is nullable with errors set to ignore, the null values
# should be numpy.nan values
result = json_normalize(
    data=missing_metadata, record_path="addresses", meta="name", errors="ignore"
)
ex_data = [
    [9562, "Morris St.", "Massillon", "OH", 44646, "Alice"],
    [8449, "Spring St.", "Elizabethton", "TN", 37643, np.nan],
]
columns = ["number", "street", "city", "state", "zip", "name"]
expected = DataFrame(ex_data, columns=columns)
tm.assert_frame_equal(result, expected)
