# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a tf.Keras model with multiple inputs and outputs."""
left_input_data = tf.constant(1., shape=[1, 3])
right_input_data = tf.constant(1., shape=[1, 3])

# Create a simple Keras model.
input_a_np = np.random.random((10, 3))
input_b_np = np.random.random((10, 3))
output_c_np = np.random.random((10, 3))
output_d_np = np.random.random((10, 2))

input_a = tf.keras.layers.Input(shape=(3,), name='input_a')
input_b = tf.keras.layers.Input(shape=(3,), name='input_b')

dense = tf.keras.layers.Dense(8, name='dense_1')
interm_a = dense(input_a)
interm_b = dense(input_b)
merged = tf.keras.layers.concatenate([interm_a, interm_b], name='merge')

output_c = tf.keras.layers.Dense(
    3, activation='softmax', name='dense_2')(
        merged)
output_d = tf.keras.layers.Dense(
    2, activation='softmax', name='dense_3')(
        merged)

model = tf.keras.models.Model(
    inputs=[input_a, input_b], outputs=[output_c, output_d])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit([input_a_np, input_b_np], [output_c_np, output_d_np], epochs=1)

# Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_keras_model(model)
tflite_model = converter.convert()

# Check values from converted model.
input_data = [left_input_data, right_input_data]
expected_value = model.predict(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, input_data)
for tf_result, tflite_result in zip(expected_value, actual_value):
    self.assertAllClose(tf_result, tflite_result, atol=1e-05)
