# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
file = datapath("io", "data", "stata", f"{file}.dta")
parsed = read_stata(file)

parsed_unordered = read_stata(file, order_categoricals=False)
for col in parsed:
    if not is_categorical_dtype(parsed[col].dtype):
        continue
    assert parsed[col].cat.ordered
    assert not parsed_unordered[col].cat.ordered
