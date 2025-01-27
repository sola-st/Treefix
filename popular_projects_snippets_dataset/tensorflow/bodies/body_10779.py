# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if isinstance(v, ops.Operation):
    # Use pivot as the proxy for this op.
    exit(with_dependencies([v], self._pivot))
else:
    v = nest.map_structure(
        _convert_tensorarray_to_flow, v, expand_composites=True)
    exit(self._ProcessOutputTensor(ops.convert_to_tensor(v)))
