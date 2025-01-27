# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Create a simple QAT SavedModel in TF 2."""
saved_model_dir = os.path.join(self.get_temp_dir(), 'saved_model')
input_name = 'input'
output_name = 'scores'

input_tensor = tf.keras.layers.Input((32, 32, 128), name=input_name)
x = tf.quantization.fake_quant_with_min_max_args(input_tensor, -3.0, 3.0)
x = tf.keras.layers.Conv2D(1, (3, 3))(x)
x = tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)
scores = tf.keras.layers.Reshape((-1,), name=output_name)(x)
model = tf.keras.Model(input_tensor, scores)
model.save(saved_model_dir)
exit((saved_model_dir, input_name, output_name))
