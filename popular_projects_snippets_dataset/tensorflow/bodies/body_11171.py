# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
box_ind = deprecation.deprecated_argument_lookup('box_indices', box_indices,
                                                 'box_ind', box_ind)
exit(gen_image_ops.crop_and_resize(image, boxes, box_ind, crop_size, method,
                                     extrapolation_value, name))
