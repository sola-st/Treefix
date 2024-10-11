# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(Cropping2D, self).__init__(**kwargs)
self.data_format = conv_utils.normalize_data_format(data_format)
if isinstance(cropping, int):
    self.cropping = ((cropping, cropping), (cropping, cropping))
elif hasattr(cropping, '__len__'):
    if len(cropping) != 2:
        raise ValueError('`cropping` should have two elements. '
                         'Found: ' + str(cropping))
    height_cropping = conv_utils.normalize_tuple(cropping[0], 2,
                                                 '1st entry of cropping')
    width_cropping = conv_utils.normalize_tuple(cropping[1], 2,
                                                '2nd entry of cropping')
    self.cropping = (height_cropping, width_cropping)
else:
    raise ValueError('`cropping` should be either an int, '
                     'a tuple of 2 ints '
                     '(symmetric_height_crop, symmetric_width_crop), '
                     'or a tuple of 2 tuples of 2 ints '
                     '((top_crop, bottom_crop), (left_crop, right_crop)). '
                     'Found: ' + str(cropping))
self.input_spec = InputSpec(ndim=4)
