# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# see gh-781
df = DataFrame({"col1": [1], "col2": ["a"], "col3": [10.1]})

expected_rows = [",col1,col2,col3", "0,1,a,10.1"]
expected_default = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv() == expected_default

expected_rows = [";col1;col2;col3", "0;1;a;10,1"]
expected_european_excel = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(decimal=",", sep=";") == expected_european_excel

expected_rows = [",col1,col2,col3", "0,1,a,10.10"]
expected_float_format_default = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(float_format="%.2f") == expected_float_format_default

expected_rows = [";col1;col2;col3", "0;1;a;10,10"]
expected_float_format = tm.convert_rows_list_to_csv_str(expected_rows)
assert (
    df.to_csv(decimal=",", sep=";", float_format="%.2f")
    == expected_float_format
)

# see gh-11553: testing if decimal is taken into account for '0.0'
df = DataFrame({"a": [0, 1.1], "b": [2.2, 3.3], "c": 1})

expected_rows = ["a,b,c", "0^0,2^2,1", "1^1,3^3,1"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(index=False, decimal="^") == expected

# same but for an index
assert df.set_index("a").to_csv(decimal="^") == expected

# same for a multi-index
assert df.set_index(["a", "b"]).to_csv(decimal="^") == expected
