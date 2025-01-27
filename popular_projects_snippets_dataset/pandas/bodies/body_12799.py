# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
data = {
    "flat1": 1,
    "dict1": {"c": 1, "d": 2},
    "nested": {"e": {"c": 1, "d": 2}, "d": 2},
}

result = nested_to_record(data)
expected = {
    "dict1.c": 1,
    "dict1.d": 2,
    "flat1": 1,
    "nested.d": 2,
    "nested.e.c": 1,
    "nested.e.d": 2,
}

assert result == expected
