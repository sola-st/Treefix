# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
d = {"a": ["\u05d0", 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
idx = pd.DataFrame(d).set_index(["a", "b"]).index
str(idx)
