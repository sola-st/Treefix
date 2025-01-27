# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH5508

# dtype getting changed?
df = DataFrame(index=Index(np.arange(1, 11)))
df["foo"] = np.zeros(10, dtype=np.float64)
df["bar"] = np.zeros(10, dtype=complex)

msg = "Must have equal len keys and value when setting with an iterable"
with pytest.raises(ValueError, match=msg):
    df[2:5] = np.arange(1, 4) * 1j
