# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_axis.py
# wrong length
msg = (
    f"Length mismatch: Expected axis has {len(obj)} elements, "
    f"new values have {len(obj)-1} elements"
)
with pytest.raises(ValueError, match=msg):
    obj.index = np.arange(len(obj) - 1)

if obj.ndim == 2:
    with pytest.raises(ValueError, match="Length mismatch"):
        obj.columns = obj.columns[::2]
