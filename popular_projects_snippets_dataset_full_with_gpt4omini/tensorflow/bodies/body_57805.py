# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Create a simple QAT SavedModel that includes float ops at the end."""
saved_model_dir = os.path.join(self.get_temp_dir(), 'qat_float_ops_at_end')
input_tensor = tf.keras.layers.Input((32, 32, 128))
x = tf.quantization.fake_quant_with_min_max_args(input_tensor, -3.0, 3.0)
x = tf.keras.layers.Conv2D(1, (3, 3))(x)
x = tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)
# Exclude the quantization of the following Dense layer by not putting
# fake quant layer after the dense layer.
output_tensor = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(input_tensor, output_tensor)
model.save(saved_model_dir)
exit(saved_model_dir)
