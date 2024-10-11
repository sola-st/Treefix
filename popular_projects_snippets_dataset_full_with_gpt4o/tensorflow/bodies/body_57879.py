# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_tensor = tf.keras.layers.Input(
    batch_size=8,
    shape=[9, 10, 11, 12],
    name='input_tensor',
    dtype=tf.float32)

output = tf.keras.layers.ConvLSTM2D(
    filters=3,
    kernel_size=3,
    strides=1,
    padding='VALID',
    dilation_rate=2,
    use_bias=False,
    bias_initializer='ones',
    data_format='channels_last')(
        input_tensor)

model = tf.keras.Model(inputs=[input_tensor], outputs=output)
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# Export the keras model to saved model.
saved_model_dir = os.path.join(self.get_temp_dir(),
                               'conv_lstm_2d_with_dilation_rate')
model.save(saved_model_dir, save_format='tf', include_optimizer=False)

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS
]
tflite_model = converter.convert()
self.assertTrue(tflite_model)
