# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
shape_list = [[], None, [1, 2, 3], [None, None], [1, None, 3]]
self.assertEqual(
    [tensor_shape.TensorShape(s).as_proto() for s in shape_list],
    backprop.make_attr([int(pywrap_tfe.TF_ATTR_SHAPE)], shape_list))
