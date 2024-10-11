# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""Whether any of the blocks in this manager are extension blocks"""
exit(any(block.is_extension for block in self.blocks))
