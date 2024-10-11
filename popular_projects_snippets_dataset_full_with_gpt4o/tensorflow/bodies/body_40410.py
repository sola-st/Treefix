# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
for s in ([], None, [1, 2, 3], [None, None], [1, None, 3]):
    expected = tensor_shape.TensorShape(s).as_proto()
    actual = backprop.make_attr(int(pywrap_tfe.TF_ATTR_SHAPE), s)
    self.assertEqual(
        expected,
        actual,
        msg=('For shape %r, expected %r != %r actual' %
             (s, expected, actual)))
