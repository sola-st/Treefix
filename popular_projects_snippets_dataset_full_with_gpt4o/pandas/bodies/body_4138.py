# Extracted from ./data/repos/pandas/pandas/tests/frame/common.py
dtypes = {"A": "int32", "B": "uint64", "C": "uint8", "D": "int64"}
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
