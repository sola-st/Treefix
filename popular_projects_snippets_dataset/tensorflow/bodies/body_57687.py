# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
model = keras.models.Sequential()
model.add(keras.layers.Dense(2, input_shape=(3,)))
if include_custom_layer:
    model.add(MyAddLayer(1.0))
model.add(keras.layers.RepeatVector(3))
model.add(keras.layers.TimeDistributed(keras.layers.Dense(3)))
model.compile(
    loss=keras.losses.MSE,
    optimizer='sgd',
    metrics=[keras.metrics.categorical_accuracy],
    sample_weight_mode='temporal')
x = np.random.random((1, 3))
y = np.random.random((1, 3, 3))
model.train_on_batch(x, y)
model.predict(x)

try:
    fd, self._keras_file = tempfile.mkstemp('.h5')
    keras.models.save_model(model, self._keras_file)
finally:
    os.close(fd)

if include_custom_layer:
    self._custom_objects = {'MyAddLayer': MyAddLayer}
