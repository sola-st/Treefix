# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 10209
df_sec = DataFrame({"A": pd.date_range("20130101", periods=5, freq="s")})
df_day = DataFrame({"A": pd.date_range("20130101", periods=5, freq="d")})

expected_rows = [
    ",A",
    "0,2013-01-01 00:00:00",
    "1,2013-01-01 00:00:01",
    "2,2013-01-01 00:00:02",
    "3,2013-01-01 00:00:03",
    "4,2013-01-01 00:00:04",
]
expected_default_sec = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_sec.to_csv() == expected_default_sec

expected_rows = [
    ",A",
    "0,2013-01-01 00:00:00",
    "1,2013-01-02 00:00:00",
    "2,2013-01-03 00:00:00",
    "3,2013-01-04 00:00:00",
    "4,2013-01-05 00:00:00",
]
expected_ymdhms_day = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_day.to_csv(date_format="%Y-%m-%d %H:%M:%S") == expected_ymdhms_day

expected_rows = [
    ",A",
    "0,2013-01-01",
    "1,2013-01-01",
    "2,2013-01-01",
    "3,2013-01-01",
    "4,2013-01-01",
]
expected_ymd_sec = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_sec.to_csv(date_format="%Y-%m-%d") == expected_ymd_sec

expected_rows = [
    ",A",
    "0,2013-01-01",
    "1,2013-01-02",
    "2,2013-01-03",
    "3,2013-01-04",
    "4,2013-01-05",
]
expected_default_day = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_day.to_csv() == expected_default_day
assert df_day.to_csv(date_format="%Y-%m-%d") == expected_default_day

# see gh-7791
#
# Testing if date_format parameter is taken into account
# for multi-indexed DataFrames.
df_sec["B"] = 0
df_sec["C"] = 1

expected_rows = ["A,B,C", "2013-01-01,0,1.0"]
expected_ymd_sec = tm.convert_rows_list_to_csv_str(expected_rows)

df_sec_grouped = df_sec.groupby([pd.Grouper(key="A", freq="1h"), "B"])
assert df_sec_grouped.mean().to_csv(date_format="%Y-%m-%d") == expected_ymd_sec
