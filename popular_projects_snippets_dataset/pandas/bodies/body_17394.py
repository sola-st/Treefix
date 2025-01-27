# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_spec_conformance.py
df = df_from_dict(
    {"x": [True, True, False], "y": [1, 2, 0], "z": [9.2, 10.5, 11.8]}
)
dfX = df.__dataframe__()

assert dfX.num_columns() == 3
assert dfX.num_rows() == 3
assert dfX.num_chunks() == 1
assert list(dfX.column_names()) == ["x", "y", "z"]
assert list(dfX.select_columns((0, 2)).column_names()) == list(
    dfX.select_columns_by_name(("x", "z")).column_names()
)
