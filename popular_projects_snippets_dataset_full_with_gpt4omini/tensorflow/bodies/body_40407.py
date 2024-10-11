# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
self.assertEqual(
    [b'a'], backprop.make_attr([int(pywrap_tfe.TF_ATTR_STRING)], ['a']))
