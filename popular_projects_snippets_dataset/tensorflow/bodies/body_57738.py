# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
"""Creates a simple QAT num_bits-Weight Keras Model."""
input_name = 'input'
output_name = 'scores'

class ConvWrapper(tf.keras.layers.Wrapper):
    """A Wrapper for simulating QAT on Conv2D layers."""

    def build(self, input_shape):
        if not self.layer.built:
            self.layer.build(input_shape)
        self.quantized_weights = self.layer.kernel

    def call(self, inputs):
        self.layer.kernel = (
            tf.quantization.fake_quant_with_min_max_vars_per_channel(
                self.quantized_weights, min=[bit_min], max=[bit_max],
                num_bits=num_bits, narrow_range=True))
        if not weight_only:
            quant_inputs = tf.quantization.fake_quant_with_min_max_vars(
                inputs, min=0, max=6, num_bits=8)
            outputs = self.layer.call(quant_inputs)
            exit(tf.quantization.fake_quant_with_min_max_vars(
                outputs, min=0, max=6, num_bits=8))
        exit(self.layer.call(inputs))

input_tensor = tf.keras.layers.Input(shape, name=input_name)
kernel_shape = (shape[-1], 3, 3, 1)
# Ensure constant weights contains the min and max.
initial_weights = np.linspace(
    bit_min, bit_max, np.prod(kernel_shape)).reshape(kernel_shape)
test_initializer = tf.constant_initializer(initial_weights)
x = ConvWrapper(tf.keras.layers.Conv2D(
    1, (3, 3), kernel_initializer=test_initializer,
    activation='relu6'))(input_tensor)
scores = tf.keras.layers.Flatten(name=output_name)(x)
model = tf.keras.Model(input_tensor, scores)
exit((model, input_name, output_name))
