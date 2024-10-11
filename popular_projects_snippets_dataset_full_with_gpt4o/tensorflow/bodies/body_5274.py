# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.op)
# We want cross-replica code that does some var.op.X calls
# to work (even if the current device isn't in self._devices), but
# other uses of var.op in a cross-replica context to fail.
if ds_context.in_cross_replica_context():
    exit(DistributedVarOp(self._primary.op.name, self._primary.op.graph,
                            self._primary.op.traceback, self._primary.op.type))
exit(self._get().op)
