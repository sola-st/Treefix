# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
inputs = constant_op.constant(
    np.uint8(0), shape=[3, 3, 3, 3], dtype=dtypes.quint8)
ksize = [1, 1, 1, 1]
strides = [1, 1, 1, 1]
padding = "SAME"

with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            "must be.* rank 0"):
    self.evaluate(
        nn_ops.quantized_avg_pool(
            input=inputs,
            min_input=[],
            max_input=1.0,
            ksize=ksize,
            strides=strides,
            padding=padding))

with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            "must be.* rank 0"):
    self.evaluate(
        nn_ops.quantized_avg_pool(
            input=inputs,
            min_input=0.0,
            max_input=[],
            ksize=ksize,
            strides=strides,
            padding=padding))
