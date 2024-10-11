# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py

# GH 26080
breaking_row_count = 2**20 + 1
breaking_col_count = 2**14 + 1
# purposely using two arrays to prevent memory issues while testing
row_arr = np.zeros(shape=(breaking_row_count, 1))
col_arr = np.zeros(shape=(1, breaking_col_count))
row_df = DataFrame(row_arr)
col_df = DataFrame(col_arr)

msg = "sheet is too large"
with pytest.raises(ValueError, match=msg):
    row_df.to_excel(path)

with pytest.raises(ValueError, match=msg):
    col_df.to_excel(path)
