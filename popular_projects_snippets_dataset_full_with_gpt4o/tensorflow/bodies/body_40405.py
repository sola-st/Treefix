# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
self.assertEqual([dtypes.float32],
                 backprop.make_attr([int(pywrap_tfe.TF_ATTR_TYPE)], [1]))
