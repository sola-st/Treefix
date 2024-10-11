# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.op)
exit(values.DistributedVarOp(self._primary.op.name,
                               self._primary.op.graph,
                               self._primary.op.traceback,
                               self._primary.op.type))
