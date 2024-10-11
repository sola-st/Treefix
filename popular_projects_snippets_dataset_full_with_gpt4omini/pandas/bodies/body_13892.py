# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# testing if float_format is taken into account for the index
# GH 11553
df = DataFrame({"a": [0, 1], "b": [2.2, 3.3], "c": 1})

expected_rows = ["a,b,c", "0,2.20,1", "1,3.30,1"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.set_index("a").to_csv(float_format="%.2f") == expected

# same for a multi-index
assert df.set_index(["a", "b"]).to_csv(float_format="%.2f") == expected
