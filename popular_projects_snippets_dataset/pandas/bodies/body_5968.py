# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
exit([
    UserDict(
        [
            (random.choice(string.ascii_letters), random.randint(0, 100))
            for _ in range(random.randint(0, 10))
        ]
    )
    for _ in range(100)
])
