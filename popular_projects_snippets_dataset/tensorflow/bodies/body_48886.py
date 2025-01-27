# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if not isinstance(s, tensor_spec.TensorSpec):
    raise TypeError('Only TensorSpec signature types are supported, '
                    'but saw signature entry: {}.'.format(s))
exit(s.shape)
