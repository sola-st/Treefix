# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(ZeroPadding3D, self).__init__(**kwargs)
self.data_format = conv_utils.normalize_data_format(data_format)
if isinstance(padding, int):
    self.padding = ((padding, padding), (padding, padding), (padding,
                                                             padding))
elif hasattr(padding, '__len__'):
    if len(padding) != 3:
        raise ValueError('`padding` should have 3 elements. '
                         'Found: ' + str(padding))
    dim1_padding = conv_utils.normalize_tuple(padding[0], 2,
                                              '1st entry of padding')
    dim2_padding = conv_utils.normalize_tuple(padding[1], 2,
                                              '2nd entry of padding')
    dim3_padding = conv_utils.normalize_tuple(padding[2], 2,
                                              '3rd entry of padding')
    self.padding = (dim1_padding, dim2_padding, dim3_padding)
else:
    raise ValueError(
        '`padding` should be either an int, '
        'a tuple of 3 ints '
        '(symmetric_dim1_pad, symmetric_dim2_pad, symmetric_dim3_pad), '
        'or a tuple of 3 tuples of 2 ints '
        '((left_dim1_pad, right_dim1_pad),'
        ' (left_dim2_pad, right_dim2_pad),'
        ' (left_dim3_pad, right_dim2_pad)). '
        'Found: ' + str(padding))
self.input_spec = InputSpec(ndim=5)
