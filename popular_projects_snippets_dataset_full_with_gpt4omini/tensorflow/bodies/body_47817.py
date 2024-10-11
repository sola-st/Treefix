# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
if len(inputs) != 2:
    raise ValueError('A `Subtract` layer should be called '
                     'on exactly 2 inputs')
exit(inputs[0] - inputs[1])
