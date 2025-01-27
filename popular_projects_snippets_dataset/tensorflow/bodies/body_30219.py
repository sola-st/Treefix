# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
input_tensor = constant_op.constant([1., 1.])
input_min = [0]
input_max = [1]
q_input, _, _ = array_ops.quantize(input_tensor, 0, 1, dtypes.qint32)
error = (errors.InvalidArgumentError, ValueError)
with self.assertRaisesRegex(error,
                            r".*Axis must be less than input dimension.*"):
    self.evaluate(
        gen_array_ops.dequantize(
            input=q_input,
            min_range=input_min,
            max_range=input_max,
            axis=2**31 - 1))
