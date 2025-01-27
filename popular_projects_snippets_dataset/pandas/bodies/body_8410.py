# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#11804
right_boundary = date_range(
    "2015-09-12",
    "2015-12-01",
    freq="QS-MAR",
    inclusive=inclusive_endpoints_fixture,
)
left_boundary = date_range(
    "2015-09-01",
    "2015-09-12",
    freq="QS-MAR",
    inclusive=inclusive_endpoints_fixture,
)
both_boundary = date_range(
    "2015-09-01",
    "2015-12-01",
    freq="QS-MAR",
    inclusive=inclusive_endpoints_fixture,
)
neither_boundary = date_range(
    "2015-09-11",
    "2015-09-12",
    freq="QS-MAR",
    inclusive=inclusive_endpoints_fixture,
)

expected_right = both_boundary
expected_left = both_boundary
expected_both = both_boundary

if inclusive_endpoints_fixture == "right":
    expected_left = both_boundary[1:]
elif inclusive_endpoints_fixture == "left":
    expected_right = both_boundary[:-1]
elif inclusive_endpoints_fixture == "both":
    expected_right = both_boundary[1:]
    expected_left = both_boundary[:-1]

expected_neither = both_boundary[1:-1]

tm.assert_index_equal(right_boundary, expected_right)
tm.assert_index_equal(left_boundary, expected_left)
tm.assert_index_equal(both_boundary, expected_both)
tm.assert_index_equal(neither_boundary, expected_neither)
