# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = simple_index
sl = index[[1, 2, 3]]
for i in sl:
    assert i == sl[sl.get_loc(i)]
