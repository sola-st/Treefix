# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
exit(self._AccumulateNTemplate(
    inputs,
    init=array_ops.zeros_like(inputs[0]),
    shape=inputs[0].get_shape(),
    validate_shape=True))
