# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Test with DEMO_G.xpt, reading full file incrementally

data_csv = pd.read_csv(file01.replace(".xpt", ".csv"))
data_csv = data_csv.set_index("SEQN")
numeric_as_float(data_csv)

with read_sas(file01, index="SEQN", chunksize=1000) as reader:
    all_data = list(reader)
data = pd.concat(all_data, axis=0)

tm.assert_frame_equal(data, data_csv, check_index_type=False)
