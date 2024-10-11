# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Tests with DEMO_G.xpt (all numeric file)

# Compare to this
data_csv = pd.read_csv(file01.replace(".xpt", ".csv"))
numeric_as_float(data_csv)

# Read full file
data = read_sas(file01, format="xport")
tm.assert_frame_equal(data, data_csv)
num_rows = data.shape[0]

# Test reading beyond end of file
with read_sas(file01, format="xport", iterator=True) as reader:
    data = reader.read(num_rows + 100)
assert data.shape[0] == num_rows

# Test incremental read with `read` method.
with read_sas(file01, format="xport", iterator=True) as reader:
    data = reader.read(10)
tm.assert_frame_equal(data, data_csv.iloc[0:10, :])

# Test incremental read with `get_chunk` method.
with read_sas(file01, format="xport", chunksize=10) as reader:
    data = reader.get_chunk()
tm.assert_frame_equal(data, data_csv.iloc[0:10, :])

# Test read in loop
m = 0
with read_sas(file01, format="xport", chunksize=100) as reader:
    for x in reader:
        m += x.shape[0]
assert m == num_rows

# Read full file with `read_sas` method
data = read_sas(file01)
tm.assert_frame_equal(data, data_csv)
