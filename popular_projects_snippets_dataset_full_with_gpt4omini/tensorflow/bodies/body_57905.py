# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

class QuantConv2DTransposedWithBiasAndActivation(tf.keras.layers.Layer):

    def build(self, input_shape):
        self.kernel = self.add_weight('kernel', (3, 3, input_shape[-1], 3))
        self.bias = self.add_weight('bias', (3,))

    def call(self, inputs):
        filters = tf.quantization.fake_quant_with_min_max_vars(
            self.kernel, -3.0, 3.0, narrow_range=True)
        filters = tf.transpose(filters, (0, 1, 3, 2))
        result = tf.nn.conv2d_transpose(inputs, filters,
                                        [*inputs.shape[:-1], 3], 1)
        result = tf.nn.bias_add(result, self.bias)
        result = tf.nn.relu(result)

        exit(tf.quantization.fake_quant_with_min_max_vars(
            result, -3.0, 3.0, narrow_range=True))

inp = tf.keras.Input(shape=(6, 8, 6), batch_size=1)
x = tf.quantization.fake_quant_with_min_max_vars(
    inp, -3.0, 3.0, narrow_range=True)
x = QuantConv2DTransposedWithBiasAndActivation()(x)

model = tf.keras.Model(inp, x)

tf_input_shape = (1, 6, 8, 6)
input_data = np.linspace(
    0, 6, np.prod(tf_input_shape)).reshape(tf_input_shape)
tf_result = model(input_data)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

converted_model = converter.convert()
tf.lite.experimental.Analyzer.analyze(model_content=converted_model)

interpreter = tf.lite.Interpreter(model_content=converted_model)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

interpreter.set_tensor(input_index, input_data.astype(np.float32))
interpreter.invoke()
tflite_result = interpreter.tensor(output_index)()

self.assertAllClose(
    [np.linalg.norm(
        tflite_result - tf_result.numpy().astype(np.float32))], [0.0])

num_float32_tensor = 0
for detail in interpreter.get_tensor_details():
    if detail['dtype'] == np.float32:
        num_float32_tensor += 1

    # There should be only 2 float tensors, input and output.
self.assertEqual(num_float32_tensor, 2)
