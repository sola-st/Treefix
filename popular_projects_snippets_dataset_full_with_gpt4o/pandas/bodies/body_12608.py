# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
url = "https://api.github.com/repos/pandas-dev/pandas/issues?per_page=5"
result = read_json(url, convert_dates=True)
assert result[field].dtype == dtype
