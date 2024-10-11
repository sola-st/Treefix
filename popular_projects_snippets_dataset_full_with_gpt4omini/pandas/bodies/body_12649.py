# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame([[1]], columns=[pd.Timedelta("1D")])
expected = f'{{"{key}":{{"0":1}}}}'
result = df.to_json(date_format=date_format)

assert result == expected
