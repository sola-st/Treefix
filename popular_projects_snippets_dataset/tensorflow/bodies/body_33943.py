# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
with ops.Graph().as_default(), context.eager_mode():
    input_value = constant_op.constant([-0.8, -0.5, 0, 0.3, 0.8, -2.0],
                                       shape=(6,),
                                       dtype=dtypes.float32),
    input_min = constant_op.constant(-127, shape=(), dtype=dtypes.float32)
    input_max = constant_op.constant(127, shape=(), dtype=dtypes.float32)
    num_bits = constant_op.constant(8, shape=(), dtype=dtypes.int32)

    quantized = array_ops.quantize_and_dequantize_v3(
        input_value,
        input_min,
        input_max,
        num_bits,
        signed_input=True,
        range_given=False)
    self.assertSequenceAlmostEqual(
        input_value[0].numpy(), quantized.numpy()[0], delta=0.05)
