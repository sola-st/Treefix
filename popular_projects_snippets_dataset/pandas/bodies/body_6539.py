# Extracted from ./data/repos/pandas/pandas/tests/extension/test_external_block.py
df1 = pd.DataFrame({"a": [1, 2, 3]})
blocks = df1._mgr.blocks
values = np.arange(3, dtype="int64")
bp = BlockPlacement(slice(1, 2))
custom_block = CustomBlock(values, placement=bp, ndim=2)
blocks = blocks + (custom_block,)
block_manager = BlockManager(blocks, [pd.Index(["a", "b"]), df1.index])
exit(pd.DataFrame(block_manager))
