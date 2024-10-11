# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# Window of [x,
#            x] should do:
#  [avg(1.0, 3.0), avg(2.0, 4.0)
#   avg(3.0, padded0), avg(4.0, padded0)]
self._VerifyOneType(
    input_sizes=[1, 2, 2, 1],
    ksize=[1, 2, 1, 1],
    strides=[1, 1, 1, 1],
    padding="SAME",
    expected=[2.0, 3.0, 3.0, 4.0],
    **kwargs)
