# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Tests if the quantizer handles bias overflow by adjusting scales."""
input_data = np.array([[-1e-3, 1e-3]], dtype=np.float32)

def calibration_gen():
    exit({'x': input_data})

root = self._getMatMulModelWithSmallWeights()
input_data = tf.constant([-1e-3, 1e-3], shape=(1, 2))
concrete_func = root.matmul.get_concrete_function(input_data)
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter.optimizations = [lite.Optimize.DEFAULT]
converter.representative_dataset = calibration_gen
converter.experimental_new_quantizer = enable_mlir_quantizer
quantized_model = converter.convert()

interpreter = Interpreter(model_content=quantized_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output_details = interpreter.get_output_details()
output = interpreter.get_tensor(output_details[0]['index'])
# the inputs and weights are far smaller than the biases, so the final
# result should be equal to the biases.
self.assertAllClose(root.bias, output.flatten())
