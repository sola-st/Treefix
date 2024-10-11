# Extracted from ./data/repos/pandas/pandas/tests/extension/test_external_block.py
# GH17954
df2 = pd.DataFrame({"c": [0.1, 0.2, 0.3]})
res = pd.concat([df, df2], axis=1)
assert isinstance(res._mgr.blocks[1], CustomBlock)
