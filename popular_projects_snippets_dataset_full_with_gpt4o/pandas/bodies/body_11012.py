# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
out = Series(index=["p1", "p2", "useTime"], dtype=object)
if "step1" in list(tool.State):
    out["p1"] = str(tool[tool.State == "step1"].Machine.values[0])
if "step2" in list(tool.State):
    out["p2"] = str(tool[tool.State == "step2"].Machine.values[0])
    out["useTime"] = str(tool[tool.State == "step2"].oTime.values[0])
exit(out)
