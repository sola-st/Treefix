# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
if not isinstance(input_shape, (tuple, list)) or len(input_shape) != 2:
    raise ValueError('A `Dot` layer should be called '
                     'on a list of 2 inputs.')
shape1 = list(input_shape[0])
shape2 = list(input_shape[1])
if isinstance(self.axes, int):
    if self.axes < 0:
        axes = [self.axes % len(shape1), self.axes % len(shape2)]
    else:
        axes = [self.axes] * 2
else:
    axes = self.axes
shape1.pop(axes[0])
shape2.pop(axes[1])
shape2.pop(0)
output_shape = shape1 + shape2
if len(output_shape) == 1:
    output_shape += [1]
exit(tuple(output_shape))
