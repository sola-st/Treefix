# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
mask = np.array([True, False])
msg = f"Boolean index has wrong length: 2 instead of {len(data)}"
with pytest.raises(IndexError, match=msg):
    data[mask]

mask = pd.array(mask, dtype="boolean")
with pytest.raises(IndexError, match=msg):
    data[mask]
