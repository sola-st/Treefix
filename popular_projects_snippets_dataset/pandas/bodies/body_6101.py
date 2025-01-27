# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# see GH-27785 take_nd with indexer of len 1 resulting in wrong ndim
df = pd.DataFrame({"A": data})
res = df.loc[[0], "A"]
assert res.ndim == 1
assert res._mgr.arrays[0].ndim == 1
if hasattr(res._mgr, "blocks"):
    assert res._mgr._block.ndim == 1
