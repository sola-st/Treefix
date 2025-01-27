# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
if num_rows is None:
    num_rows = N

exit(SingleBlockManager(
    create_block(typestr, placement=slice(0, num_rows), item_shape=()),
    Index(np.arange(num_rows)),
))
