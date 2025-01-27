# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/quantized_ops_test.py
num_rows = 100
num_columns = 3547
random_input = np.random.normal(128.0, 10.0, [num_rows, num_columns])
with self.session() as session:
    with ops.device("CPU"):
        test_input = ops.convert_to_tensor(random_input, dtype=dtypes.float32)
        transposed_input = array_ops.transpose(test_input, [1, 0])
        quantized_input = array_ops.quantize(transposed_input, 0.0, 255.0,
                                             dtypes.quint8)
        packed_input = self.pack_uint8_r2_to_uint32(quantized_input.output)
    with self.test_scope():
        transposed_quantized_output = xla.dequantize(packed_input, 0.0, 255.0,
                                                     "MIN_COMBINED", True)
        quantized_output = array_ops.slice(transposed_quantized_output, [0, 0],
                                           [num_rows, num_columns])

    value = session.run(quantized_output)
self.assertAllClose(value, random_input, 1.0)
