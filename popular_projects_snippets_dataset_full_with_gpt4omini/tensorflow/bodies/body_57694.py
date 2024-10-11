# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
a = keras.layers.Input(shape=(3,), name='input_a')
b = keras.layers.Input(shape=(3,), name='input_b')
dense = keras.layers.Dense(4, name='dense')
c = dense(a)
d = dense(b)
e = keras.layers.Dropout(0.5, name='dropout')(c)

model = keras.models.Model([a, b], [d, e])
model.compile(
    loss=keras.losses.MSE,
    optimizer='sgd',
    metrics=[keras.metrics.mae],
    loss_weights=[1., 0.5])

input_a_np = np.random.random((10, 3))
input_b_np = np.random.random((10, 3))
output_d_np = np.random.random((10, 4))
output_e_np = np.random.random((10, 4))
model.train_on_batch([input_a_np, input_b_np], [output_d_np, output_e_np])

model.predict([input_a_np, input_b_np], batch_size=5)
fd, self._keras_file = tempfile.mkstemp('.h5')
try:
    keras.models.save_model(model, self._keras_file)
finally:
    os.close(fd)
