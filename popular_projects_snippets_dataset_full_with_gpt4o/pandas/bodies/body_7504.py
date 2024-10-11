# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
index = MultiIndex(
    levels=[[0, 1], [0, 1], [0, 1], [0]],
    codes=[
        [0, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ],
)

result = index.format()
assert result[3] == "1  0  0  0"
