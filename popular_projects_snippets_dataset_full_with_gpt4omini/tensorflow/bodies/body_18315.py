# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""True if op was created inside the pfor loop body."""
assert isinstance(op, ops.Operation)
# Note that we use self._pfor_op_ids for the check and not self._pfor_ops
# since it appears there tensorflow API could return different python
# objects representing the same Operation node.
exit(op._id in self._pfor_op_ids)
