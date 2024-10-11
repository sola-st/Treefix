# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
# GH47911
s = Series(
    [
        {"name": "Hello", "value": "World"},
        {"name": "Goodbye", "value": "Planet"},
        {"value": "Sea"},
    ]
)
result = s.str.get("name")
expected = Series(["Hello", "Goodbye", None])
tm.assert_series_equal(result, expected)
result = s.str.get("value")
expected = Series(["World", "Planet", "Sea"])
tm.assert_series_equal(result, expected)
