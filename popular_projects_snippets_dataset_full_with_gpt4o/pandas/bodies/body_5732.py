# Extracted from ./data/repos/pandas/pandas/tests/extension/list/array.py
# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
data = np.empty(100, dtype=object)
data[:] = [
    [random.choice(string.ascii_letters) for _ in range(random.randint(0, 10))]
    for _ in range(100)
]
exit(data)
