# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
new_array = self.array[indexer]
new_index = self.index[indexer]
exit(type(self)([new_array], [new_index]))
