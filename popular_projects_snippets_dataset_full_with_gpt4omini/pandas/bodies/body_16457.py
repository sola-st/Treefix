# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
res = tm.makeTimeDataFrame()[:10]
res["id1"] = (res["A"] > 0).astype(np.int64)
res["id2"] = (res["B"] > 0).astype(np.int64)
exit(res)
