# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
for v in data.columns:
    if data[v].dtype is np.dtype("int64"):
        data[v] = data[v].astype(np.float64)
