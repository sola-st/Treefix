# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
shape = input_shape
for layer in self.layers:
    shape = layer.compute_output_shape(shape)
exit(shape)
