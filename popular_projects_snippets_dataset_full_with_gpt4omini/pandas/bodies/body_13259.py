# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Test with SSHSV1_A.xpt, read as a binary file

# Compare to this
data_csv = pd.read_csv(file02.replace(".xpt", ".csv"))
numeric_as_float(data_csv)

with open(file02, "rb") as fd:
    with td.file_leak_context():
        # GH#35693 ensure that if we pass an open file, we
        #  dont incorrectly close it in read_sas
        data = read_sas(fd, format="xport")

tm.assert_frame_equal(data, data_csv)
