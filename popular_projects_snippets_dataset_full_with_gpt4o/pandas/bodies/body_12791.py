# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# see gh-30148
# should not raise TypeError
result = json_normalize(
    [
        {"state": "Texas", "info": nulls_fixture},
        {"state": "Florida", "info": [{"i": 2}]},
    ],
    record_path=["info"],
)
expected = DataFrame({"i": 2}, index=[0])
tm.assert_equal(result, expected)
