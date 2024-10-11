# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
if ((not isinstance(input_shape, (tuple, list))) or
    (not isinstance(input_shape[0], (tuple, list)))):
    # The tf_utils.shape_type_conversion decorator turns tensorshapes
    # into tuples, so we need to verify that `input_shape` is a list/tuple,
    # *and* that the individual elements are themselves shape tuples.
    raise ValueError('A `Concatenate` layer should be called '
                     'on a list of inputs.')
input_shapes = input_shape
output_shape = list(input_shapes[0])
for shape in input_shapes[1:]:
    if output_shape[self.axis] is None or shape[self.axis] is None:
        output_shape[self.axis] = None
        break
    output_shape[self.axis] += shape[self.axis]
exit(tuple(output_shape))
