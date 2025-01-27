# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
ymd = multiindex_year_month_day_dataframe_random_data

df = ymd[:5].T
df[2000, 1, 10] = df[2000, 1, 7]
assert isinstance(df.columns, MultiIndex)
assert (df[2000, 1, 10] == df[2000, 1, 7]).all()
