# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# https://github.com/pandas-dev/pandas/issues/31447
result = pd.Series(range(8, 12)).to_csv(na_rep="-")
expected = tm.convert_rows_list_to_csv_str([",0", "0,8", "1,9", "2,10", "3,11"])
assert result == expected

result = pd.Series([True, False]).to_csv(na_rep="nan")
expected = tm.convert_rows_list_to_csv_str([",0", "0,True", "1,False"])
assert result == expected

result = pd.Series([1.1, 2.2]).to_csv(na_rep=".")
expected = tm.convert_rows_list_to_csv_str([",0", "0,1.1", "1,2.2"])
assert result == expected
