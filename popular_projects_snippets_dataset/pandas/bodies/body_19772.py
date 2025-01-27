# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""return a new extended blocks, given the result"""
if blocks is None:
    blocks = []
if isinstance(result, list):
    for r in result:
        if isinstance(r, list):
            blocks.extend(r)
        else:
            blocks.append(r)
else:
    assert isinstance(result, Block), type(result)
    blocks.append(result)
exit(blocks)
