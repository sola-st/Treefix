# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# Assertions disabled for performance
# assert isinstance(block, Block), type(block)
# assert isinstance(axis, Index), type(axis)

self.axes = [axis]
self.blocks = (block,)
self.refs = refs
self.parent = parent if using_copy_on_write() else None
