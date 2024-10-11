# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
exit(self._AccumulateNTemplate(
    inputs,
    init=array_ops.zeros(
        shape=inputs[0].get_shape(), dtype=inputs[0].dtype.base_dtype),
    shape=inputs[0].get_shape(),
    validate_shape=True))
