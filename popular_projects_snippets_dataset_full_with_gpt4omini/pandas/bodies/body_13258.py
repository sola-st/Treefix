# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Test with SSHSV1_A.xpt

# Compare to this
data_csv = pd.read_csv(file02.replace(".xpt", ".csv"))
numeric_as_float(data_csv)

data = read_sas(file02)
tm.assert_frame_equal(data, data_csv)
