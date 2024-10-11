# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 43394
start = "2021-09-02"
end = "2021-09-02"
result = date_range(
    start=start, end=end, freq="D", inclusive=inclusive_endpoints_fixture
)

both_range = date_range(start=start, end=end, freq="D", inclusive="both")
if inclusive_endpoints_fixture == "neither":
    expected = both_range[1:-1]
elif inclusive_endpoints_fixture in ("left", "right", "both"):
    expected = both_range[:]

tm.assert_index_equal(result, expected)
