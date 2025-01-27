# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
num_elements = 1
for dim_size in shape:
    num_elements *= dim_size
x = self._PRNG.rand(num_elements) * 1000
exit(x.reshape(shape))
