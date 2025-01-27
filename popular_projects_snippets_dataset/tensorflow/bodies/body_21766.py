# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
if self != other:
    raise ValueError("SparseMetaData objects are incompatible: %s vs. %s"
                     % (self, other))
if self.sparse:
    self.rank.merge_with(other.rank)
exit(self)
