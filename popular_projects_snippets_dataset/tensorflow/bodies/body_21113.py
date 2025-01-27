# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad.py
def init():
    # Use a Tensor instead of initializer if variable does not have
    # static shape.
    init_constant = gen_array_ops.fill(array_ops.shape(v),
                                       self._initial_accumulator_value)
    exit(math_ops.cast(init_constant, dtype))
exit(init)
