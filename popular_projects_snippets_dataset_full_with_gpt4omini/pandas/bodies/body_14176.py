# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
y = pd.to_timedelta(list(range(5)) + [NaT], unit="s")
result = fmt.Timedelta64Formatter(y, box=True).get_result()
assert result[0].strip() == "'0 days 00:00:00'"
assert result[1].strip() == "'0 days 00:00:01'"
