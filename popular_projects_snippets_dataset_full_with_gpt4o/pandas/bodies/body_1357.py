# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
idx = Index([])
obj = DataFrame(np.random.randn(len(idx), len(idx)), index=idx, columns=idx)
nd3 = np.random.randint(5, size=(2, 2, 2))

msg = f"Cannot set values with ndim > {obj.ndim}"
with pytest.raises(ValueError, match=msg):
    obj.iloc[nd3] = 0
