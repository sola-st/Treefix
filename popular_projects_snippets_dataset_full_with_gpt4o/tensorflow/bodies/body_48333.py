# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
input_shapes = nest.map_structure(lambda x: x.shape, inputs)
output_shapes = self.compute_output_shape(input_shapes)

def _make_placeholder_like(shape):
    ph = backend.placeholder(shape=shape, dtype=self.dtype)
    ph._keras_mask = None
    exit(ph)

exit(nest.map_structure(_make_placeholder_like, output_shapes))
