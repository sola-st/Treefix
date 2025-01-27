# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/calibrator/integration_test/custom_aggregator_op_test.py
with self.test_session():
    quantize_model_wrapper.clear_calibrator()
    input_tensor = array_ops.constant([1.0, 2.0, 3.0, 4.0, 5.0],
                                      dtypes.float32)
    aggregator = custom_aggregator_op_wrapper.custom_aggregator(
        input_tensor, '1')
    self.assertAllEqual(self.evaluate(aggregator), [1.0, 2.0, 3.0, 4.0, 5.0])
    min_val = quantize_model_wrapper.get_min_from_calibrator('1')
    max_val = quantize_model_wrapper.get_max_from_calibrator('1')
    self.assertAllEqual((min_val, max_val), (1.0, 5.0))
