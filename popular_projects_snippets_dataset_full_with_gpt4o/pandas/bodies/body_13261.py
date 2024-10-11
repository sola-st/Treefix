# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Test with paxraw_d_short.xpt, a shortened version of:
# http://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PAXRAW_D.ZIP
# This file has truncated floats (5 bytes in this case).

# GH 11713

data_csv = pd.read_csv(file04.replace(".xpt", ".csv"))

data = read_sas(file04, format="xport")
tm.assert_frame_equal(data.astype("int64"), data_csv)
