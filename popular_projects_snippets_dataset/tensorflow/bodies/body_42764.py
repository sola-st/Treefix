# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
self.assertEqual(constant_op.constant(u"asdf").numpy(), b"asdf")
