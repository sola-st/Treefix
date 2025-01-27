# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with context.eager_mode():
    inputs = constant_op.constant([[[1], [2], [3], [4]]],
                                  dtype=dtypes.float32)
    # Tests that slicing an EagerTensor doesn't leak memory
    inputs[0]  # pylint: disable=pointless-statement
