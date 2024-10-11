# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
bit_max = (1 << (num_bits - 1)) - 1
bit_min = -bit_max
tf_input_shape = (5, 5, 3)
tflite_input_shape = (1,) + tf_input_shape
model, input_name, output_name = (self._createV2QATLowBitKerasModel(
    tf_input_shape, weight_only, num_bits, bit_min, bit_max))
input_data = np.linspace(
    0, 6, np.prod(tflite_input_shape)).reshape(tflite_input_shape)
tf_result = model(input_data)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
if low_bit:
    converter._experimental_low_bit_qat = True
tflite_model = converter.convert()
result = self._evaluateTFLiteModelUsingSignatureDef(
    tflite_model, 'serving_default',
    {input_name: input_data.astype(np.float32)})[output_name]
self.assertAllClose(
    [np.linalg.norm(result - tf_result.numpy().astype(np.float32))], [0.0])
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
num_8bit_activations = 0
num_8bit_weights = 0
kernel_name = ('model/conv_wrapper/Conv2D;model/conv_wrapper/'
               'FakeQuantWithMinMaxVarsPerChannel')

for detail in interpreter.get_tensor_details():
    if (detail['dtype'] == np.int8 and detail['name'] and
        detail['name'] == kernel_name):
        num_8bit_weights += 1
        weights = interpreter.get_tensor(detail['index'])
        if low_bit:
            self.assertFalse((bit_min > weights).any() or
                             (weights > bit_max).any())
        else:
            self.assertTrue((bit_min > weights).any() or
                            (weights > bit_max).any())
        self.assertIn('scales', detail['quantization_parameters'])
        if low_bit and detail['quantization_parameters']['scales']:
            self.assertAllClose(
                detail['quantization_parameters']['scales'], [1.0])
    elif detail['dtype'] == np.int8 and detail['name']:
        self.assertFalse(weight_only)
        self.assertIn('scales', detail['quantization_parameters'])
        if detail['quantization_parameters']['scales']:
            self.assertAllClose(
                detail['quantization_parameters']['scales'], [6/255])
        num_8bit_activations += 1

self.assertEqual(num_8bit_weights, 0 if weight_only and not low_bit else 1)
# 3 activations with full integer: conv_input, conv_output, reshape_output
self.assertEqual(num_8bit_activations, 0 if weight_only else 3)
