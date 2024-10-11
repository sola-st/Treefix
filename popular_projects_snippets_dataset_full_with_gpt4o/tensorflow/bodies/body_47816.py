# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
super(Subtract, self).build(input_shape)
if len(input_shape) != 2:
    raise ValueError('A `Subtract` layer should be called '
                     'on exactly 2 inputs')
