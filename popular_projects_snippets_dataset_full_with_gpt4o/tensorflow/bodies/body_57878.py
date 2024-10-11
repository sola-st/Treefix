# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test saved model with non stateful ConvLSTM2D keras layer."""
# Create keras model
model = tf.keras.Sequential([
    tf.keras.layers.ConvLSTM2D(
        32, (3, 3),
        padding='same',
        return_sequences=True,
        stateful=False,
        batch_input_shape=(1, 1, 10, 10, 1))
])
model.compile()

# Export the keras model to saved model.
saved_model_dir = os.path.join(self.get_temp_dir(), 'conv_lstm_2d')
model.save(saved_model_dir, save_format='tf', include_optimizer=False)

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS
]
tflite_model = converter.convert()
self.assertTrue(tflite_model)
