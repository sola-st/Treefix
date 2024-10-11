# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
input_tensor = [2.5, 2.5]
input_min = [0, 0]
input_max = [1, 1]
# When eager_op_as_function mode is enabled XLA auto-clustering kicks in.
# XLA raises an UnimplementedError on invalid axis.
error_message_pattern = (r"Shape must be at least rank 11 but is rank "
                         r"1|invalid axis")
# TODO(b/171260356): Eager mode and graph mode throw different error types
error = (errors.InvalidArgumentError, ValueError, errors.UnimplementedError)
with self.assertRaisesRegex(error, error_message_pattern):
    self.evaluate(
        array_ops.quantize_and_dequantize_v2(
            input=input_tensor,
            input_min=input_min,
            input_max=input_max,
            axis=10))
