# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if (self._is_replicated_or_sharded_to_logical_cores() and
    tpu_util.enclosing_tpu_context() is None):
    exit(self._primary.device)
exit(super(TPUMirroredVariable, self).device)
