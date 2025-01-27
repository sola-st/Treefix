# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
input_value = constant_op.constant([-0.8, -0.5, 0, 0.3, 0.8, -2.0],
                                   shape=(6,),
                                   dtype=dtypes.float32),
input_min = constant_op.constant(-127, shape=(), dtype=dtypes.float32)
input_max = constant_op.constant(127, shape=(), dtype=dtypes.float32)
# Tensor with invalid shape and invalid number of elements.
num_bits = constant_op.constant([], shape=(0,), dtype=dtypes.int32)

# Test that running the op raises error. It raises different errors
# depending on whether the shape inference is run first or the op's
# Compute() is run first.
try:
    array_ops.quantize_and_dequantize_v3(
        input_value, input_min, input_max, num_bits, signed_input=True)
except Exception as ex:  # pylint: disable=broad-except
    if isinstance(ex, errors.InvalidArgumentError):
        self.assertRegex(str(ex), "The `num_bits` tensor should be a scalar.")
    elif isinstance(ex, ValueError):
        self.assertRegex(str(ex), "Shape must be rank 0")
    else:
        self.fail(
            "Raised exception other than expected: %s. "
            "Expected exceptions are errors.InvalidArgumentError or ValueError",
            ex.__name__)
else:
    self.fail(
        "Did not raise an exception where it is expected to raise either "
        "a ValueError or errors.InvalidArgumentError.")
