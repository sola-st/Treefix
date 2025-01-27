# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
index = MultiIndex(
    levels=[[0, 1], [0, 1]], codes=[[0, 0, 1, 1], [0, 1, 0, 1]], names=[0, 1]
)
index.format(names=True)
