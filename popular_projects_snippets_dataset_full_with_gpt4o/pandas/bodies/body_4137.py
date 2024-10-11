# Extracted from ./data/repos/pandas/pandas/tests/frame/common.py
# float16 are most likely to be upcasted to float32
dtypes = {"A": "float32", "B": "float32", "C": "float16", "D": "float64"}
if isinstance(dtype, str):
    dtypes = {k: dtype for k, v in dtypes.items()}
elif isinstance(dtype, dict):
    dtypes.update(dtype)
if dtypes.get("A"):
    assert df.dtypes["A"] == dtypes["A"]
if dtypes.get("B"):
    assert df.dtypes["B"] == dtypes["B"]
if dtypes.get("C"):
    assert df.dtypes["C"] == dtypes["C"]
if dtypes.get("D"):
    assert df.dtypes["D"] == dtypes["D"]
