# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# See gh-11934 & gh-6415
data = ["20100102 121314", "20100102 121315"]
expected_data = [
    Timestamp("2010-01-02 12:13:14", tz="utc"),
    Timestamp("2010-01-02 12:13:15", tz="utc"),
]

result = to_datetime(
    init_constructor(data), format="%Y%m%d %H%M%S", utc=True, cache=cache
)
expected = end_constructor(expected_data)
tm.assert_equal(result, expected)
