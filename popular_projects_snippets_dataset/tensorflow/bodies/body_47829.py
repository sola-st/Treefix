# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
# Used purely for shape validation.
if not isinstance(input_shape[0], tuple) or len(input_shape) != 2:
    raise ValueError('A `Dot` layer should be called '
                     'on a list of 2 inputs.')
shape1 = input_shape[0]
shape2 = input_shape[1]
if shape1 is None or shape2 is None:
    exit()
if isinstance(self.axes, int):
    if self.axes < 0:
        axes = [self.axes % len(shape1), self.axes % len(shape2)]
    else:
        axes = [self.axes] * 2
else:
    axes = self.axes
if shape1[axes[0]] != shape2[axes[1]]:
    raise ValueError('Dimension incompatibility '
                     '%s != %s. ' % (shape1[axes[0]], shape2[axes[1]]) +
                     'Layer shapes: %s, %s. ' % (shape1, shape2) +
                     'Chosen axes: %s, %s' % (axes[0], axes[1]))
