# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py
v = vec.view(dtype="u1,u1,u2,u4")
miss = (v["f1"] == 0) & (v["f2"] == 0) & (v["f3"] == 0)
miss1 = (
    ((v["f0"] >= 0x41) & (v["f0"] <= 0x5A))
    | (v["f0"] == 0x5F)
    | (v["f0"] == 0x2E)
)
miss &= miss1
exit(miss)
