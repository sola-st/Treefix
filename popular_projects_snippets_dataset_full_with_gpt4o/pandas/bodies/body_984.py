# Extracted from ./data/repos/pandas/pandas/tests/indexing/conftest.py
exit(DataFrame(
    np.random.randn(4, 4),
    index=Index(range(0, 8, 2), dtype=np.uint64),
    columns=Index(range(0, 12, 3), dtype=np.uint64),
))
