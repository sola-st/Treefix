# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Tests with DEMO_G.xpt using index (all numeric file)

# Compare to this
data_csv = pd.read_csv(file01.replace(".xpt", ".csv"))
data_csv = data_csv.set_index("SEQN")
numeric_as_float(data_csv)

# Read full file
data = read_sas(file01, index="SEQN", format="xport")
tm.assert_frame_equal(data, data_csv, check_index_type=False)

# Test incremental read with `read` method.
with read_sas(file01, index="SEQN", format="xport", iterator=True) as reader:
    data = reader.read(10)
tm.assert_frame_equal(data, data_csv.iloc[0:10, :], check_index_type=False)

# Test incremental read with `get_chunk` method.
with read_sas(file01, index="SEQN", format="xport", chunksize=10) as reader:
    data = reader.get_chunk()
tm.assert_frame_equal(data, data_csv.iloc[0:10, :], check_index_type=False)
