# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(ZeroPadding2D, self).__init__(**kwargs)
self.data_format = conv_utils.normalize_data_format(data_format)
if isinstance(padding, int):
    self.padding = ((padding, padding), (padding, padding))
elif hasattr(padding, '__len__'):
    if len(padding) != 2:
        raise ValueError('`padding` should have two elements. '
                         'Found: ' + str(padding))
    height_padding = conv_utils.normalize_tuple(padding[0], 2,
                                                '1st entry of padding')
    width_padding = conv_utils.normalize_tuple(padding[1], 2,
                                               '2nd entry of padding')
    self.padding = (height_padding, width_padding)
else:
    raise ValueError('`padding` should be either an int, '
                     'a tuple of 2 ints '
                     '(symmetric_height_pad, symmetric_width_pad), '
                     'or a tuple of 2 tuples of 2 ints '
                     '((top_pad, bottom_pad), (left_pad, right_pad)). '
                     'Found: ' + str(padding))
self.input_spec = InputSpec(ndim=4)
