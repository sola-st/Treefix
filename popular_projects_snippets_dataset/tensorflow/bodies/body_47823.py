# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
# Used purely for shape validation.
if not isinstance(input_shape[0], tuple) or len(input_shape) < 1:
    raise ValueError('A `Concatenate` layer should be called '
                     'on a list of at least 1 input.')
if all(shape is None for shape in input_shape):
    exit()
reduced_inputs_shapes = [list(shape) for shape in input_shape]
shape_set = set()
for i in range(len(reduced_inputs_shapes)):
    del reduced_inputs_shapes[i][self.axis]
    shape_set.add(tuple(reduced_inputs_shapes[i]))

if len(shape_set) != 1:
    err_msg = ('A `Concatenate` layer requires inputs with matching shapes '
               'except for the concat axis. Got inputs shapes: %s' %
               input_shape)
    # Make sure all the shapes have same ranks.
    ranks = set(len(shape) for shape in shape_set)
    if len(ranks) != 1:
        raise ValueError(err_msg)
    # Get the only rank for the set.
    (rank,) = ranks
    for axis in range(rank):
        # Skip the Nones in the shape since they are dynamic, also the axis for
        # concat has been removed above.
        unique_dims = set(
            shape[axis] for shape in shape_set if shape[axis] is not None)
        if len(unique_dims) > 1:
            raise ValueError(err_msg)
