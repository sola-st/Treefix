# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# see gh-11553
#
# Testing if NaN values are correctly represented in the index.
df = DataFrame({"a": [0, np.NaN], "b": [0, 1], "c": [2, 3]})
expected_rows = ["a,b,c", "0.0,0,2", "_,1,3"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)

assert df.set_index("a").to_csv(na_rep="_") == expected
assert df.set_index(["a", "b"]).to_csv(na_rep="_") == expected

# now with an index containing only NaNs
df = DataFrame({"a": np.NaN, "b": [0, 1], "c": [2, 3]})
expected_rows = ["a,b,c", "_,0,2", "_,1,3"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)

assert df.set_index("a").to_csv(na_rep="_") == expected
assert df.set_index(["a", "b"]).to_csv(na_rep="_") == expected

# check if na_rep parameter does not break anything when no NaN
df = DataFrame({"a": 0, "b": [0, 1], "c": [2, 3]})
expected_rows = ["a,b,c", "0,0,2", "0,1,3"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)

assert df.set_index("a").to_csv(na_rep="_") == expected
assert df.set_index(["a", "b"]).to_csv(na_rep="_") == expected

csv = pd.Series(["a", pd.NA, "c"]).to_csv(na_rep="ZZZZZ")
expected = tm.convert_rows_list_to_csv_str([",0", "0,a", "1,ZZZZZ", "2,c"])
assert expected == csv
