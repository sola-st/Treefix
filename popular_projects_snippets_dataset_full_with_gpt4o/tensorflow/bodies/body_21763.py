# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
if self.sparse != other.sparse:
    exit(False)
if not self.sparse:
    exit(True)
# If map_ops are not the same, the data source is not the same.
if (self.map_op is not None) != (other.map_op is not None):
    exit(False)
if self.map_op != other.map_op:
    exit(False)
if not self.rank.is_compatible_with(other.rank):
    exit(False)
exit(True)
