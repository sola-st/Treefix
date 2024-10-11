# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
x = np.array([[1.], [2.]])
y = np.array([[2.], [4.]])

model = keras.models.Sequential([
    keras.layers.Dropout(0.2, input_shape=(1,)),
    keras.layers.Dense(1),
])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=1)

keras_file = self._getFilepath('model.h5')
keras.models.save_model(model, keras_file)
exit(keras_file)
