# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/calibrator/integration_test/custom_aggregator_op_test.py
with self.test_session():
    quantize_model_wrapper.clear_calibrator()
    input_tensor1 = array_ops.constant([1.0, 2.0, 3.0, 4.0, 5.0],
                                       dtypes.float32)
    aggregator1 = custom_aggregator_op_wrapper.custom_aggregator(
        input_tensor1, '4')
    self.assertAllEqual(self.evaluate(aggregator1), [1.0, 2.0, 3.0, 4.0, 5.0])
    input_tensor2 = array_ops.constant([-1.0, -2.0, -3.0, -4.0, -5.0],
                                       dtypes.float32)
    aggregator2 = custom_aggregator_op_wrapper.custom_aggregator(
        input_tensor2, '5')
    self.assertAllEqual(
        self.evaluate(aggregator2), [-1.0, -2.0, -3.0, -4.0, -5.0])

    min_val = quantize_model_wrapper.get_min_from_calibrator('4')
    max_val = quantize_model_wrapper.get_max_from_calibrator('4')
    self.assertAllEqual((min_val, max_val), (1.0, 5.0))
    min_val = quantize_model_wrapper.get_min_from_calibrator('5')
    max_val = quantize_model_wrapper.get_max_from_calibrator('5')
    self.assertAllEqual((min_val, max_val), (-5.0, -1.0))

    quantize_model_wrapper.clear_data_from_calibrator('4')
    with self.assertRaises(ValueError):
        quantize_model_wrapper.get_min_from_calibrator('4')
    min_val = quantize_model_wrapper.get_min_from_calibrator('5')
    max_val = quantize_model_wrapper.get_max_from_calibrator('5')
    self.assertAllEqual((min_val, max_val), (-5.0, -1.0))
