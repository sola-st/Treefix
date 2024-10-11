# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
data = {"flat1": 1, "dict1": {"c": 1, "d": 2}}

result = nested_to_record(data)
expected = {"dict1.c": 1, "dict1.d": 2, "flat1": 1}

assert result == expected
