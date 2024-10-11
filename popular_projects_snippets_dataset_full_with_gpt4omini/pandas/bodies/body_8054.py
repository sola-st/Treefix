# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
bool_index = np.ones(len(index), dtype=bool)
bool_index[5:30:2] = False

sub_index = index[bool_index]

for i, val in enumerate(sub_index):
    assert sub_index.get_loc(val) == i

sub_index = index[list(bool_index)]
for i, val in enumerate(sub_index):
    assert sub_index.get_loc(val) == i
