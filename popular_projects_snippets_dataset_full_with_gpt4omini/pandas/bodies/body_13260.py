# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Test with DRXFCD_G.xpt (contains text and numeric variables)

# Compare to this
data_csv = pd.read_csv(file03.replace(".xpt", ".csv"))

data = read_sas(file03, encoding="utf-8")
tm.assert_frame_equal(data, data_csv)
