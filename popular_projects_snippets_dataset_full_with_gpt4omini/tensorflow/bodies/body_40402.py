# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
typ = backprop.op_attr_type('Add', 'T')
self.assertEqual(typ, int(pywrap_tfe.TF_ATTR_TYPE))
