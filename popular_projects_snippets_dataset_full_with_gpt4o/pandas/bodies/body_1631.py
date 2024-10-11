# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

data = ["2022-01-02", "2022-01-03", "2022-01-04", fill_val.date()]
index = DatetimeIndex(data, tz=fill_val.tz, dtype=exp_dtype)
df = DataFrame([10, 11, 12, 14], columns=["a"], index=index)
# adding new row using an unexisting datetime-like str index
df.loc["2022-01-08", "a"] = 13

data.append("2022-01-08")
expected_index = DatetimeIndex(data, dtype=exp_dtype)
tm.assert_index_equal(df.index, expected_index, exact=True)
