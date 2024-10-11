# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
input_shapes = nest.map_structure(lambda x: x.shape, inputs)
output_shapes = self.compute_output_shape(input_shapes)
# Convert to TensorShape so that nest.map_structure will not map into
# individual dim of the shape.
output_shapes = tf_utils.convert_shapes(output_shapes, to_tuples=False)

def _make_placeholder_like(shape):
    ph = backend.placeholder(shape=shape, dtype=self.dtype)
    ph._keras_mask = None
    exit(ph)
exit(nest.map_structure(_make_placeholder_like, output_shapes))
