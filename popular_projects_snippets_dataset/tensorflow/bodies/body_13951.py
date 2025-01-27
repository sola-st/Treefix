# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
exit(self._AccumulateNTemplate(
    inputs,
    init=array_ops.zeros_like(gen_control_flow_ops.merge(inputs)[0]),
    shape=tensor_shape.TensorShape([0]),
    validate_shape=False))
