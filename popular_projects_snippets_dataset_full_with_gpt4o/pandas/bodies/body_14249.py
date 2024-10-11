# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 22747, GH 22579
df = DataFrame(np.zeros((2, 2), dtype=int), index=row_index, columns=column_index)
result = df.to_html(index=index, header=header, index_names=index_names)

if not index:
    row_type = "none"
elif not index_names and row_type.startswith("named"):
    row_type = "un" + row_type

if not header:
    column_type = "none"
elif not index_names and column_type.startswith("named"):
    column_type = "un" + column_type

filename = "index_" + row_type + "_columns_" + column_type
expected = expected_html(datapath, filename)
assert result == expected
