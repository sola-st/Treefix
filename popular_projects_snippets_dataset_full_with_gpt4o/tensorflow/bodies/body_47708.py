# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(Cropping3D, self).__init__(**kwargs)
self.data_format = conv_utils.normalize_data_format(data_format)
if isinstance(cropping, int):
    self.cropping = ((cropping, cropping), (cropping, cropping), (cropping,
                                                                  cropping))
elif hasattr(cropping, '__len__'):
    if len(cropping) != 3:
        raise ValueError('`cropping` should have 3 elements. '
                         'Found: ' + str(cropping))
    dim1_cropping = conv_utils.normalize_tuple(cropping[0], 2,
                                               '1st entry of cropping')
    dim2_cropping = conv_utils.normalize_tuple(cropping[1], 2,
                                               '2nd entry of cropping')
    dim3_cropping = conv_utils.normalize_tuple(cropping[2], 2,
                                               '3rd entry of cropping')
    self.cropping = (dim1_cropping, dim2_cropping, dim3_cropping)
else:
    raise ValueError(
        '`cropping` should be either an int, '
        'a tuple of 3 ints '
        '(symmetric_dim1_crop, symmetric_dim2_crop, symmetric_dim3_crop), '
        'or a tuple of 3 tuples of 2 ints '
        '((left_dim1_crop, right_dim1_crop),'
        ' (left_dim2_crop, right_dim2_crop),'
        ' (left_dim3_crop, right_dim2_crop)). '
        'Found: ' + str(cropping))
self.input_spec = InputSpec(ndim=5)
