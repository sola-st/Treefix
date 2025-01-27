# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
cat = Categorical(["A", "B", "C"])
df = DataFrame(cat)
blk = df._mgr.blocks[0]

# matching dtype
assert blk.should_store(cat)
assert blk.should_store(cat[:-1])

# different dtype
assert not blk.should_store(cat.as_ordered())

# ndarray instead of Categorical
assert not blk.should_store(np.asarray(cat))
