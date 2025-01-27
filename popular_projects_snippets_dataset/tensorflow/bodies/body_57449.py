# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
"""Returns a functional Keras model with output shapes [[1, 1], [1, 2]]."""
input_tensor = keras.layers.Input(shape=(1,))
output1 = keras.layers.Dense(1, name='b')(input_tensor)
output2 = keras.layers.Dense(2, name='a')(input_tensor)
model = keras.models.Model(inputs=input_tensor, outputs=[output1, output2])

keras_file = self._getFilepath('functional_model.h5')
keras.models.save_model(model, keras_file)
exit(keras_file)
