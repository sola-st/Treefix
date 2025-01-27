# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
blk = create_block(typ, data)
assert_block_equal(tm.round_trip_pickle(blk), blk)
