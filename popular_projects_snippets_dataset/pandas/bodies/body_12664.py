# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH41174
result = data.to_json()
assert result == expected
