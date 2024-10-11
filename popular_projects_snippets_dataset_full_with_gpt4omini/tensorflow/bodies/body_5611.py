# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
self.assertIsInstance(v.name, str)
# _shared_name is also part of the interface. E.g. it's used in optimizer to
# determine slot variable key.
self.assertIsInstance(v._shared_name, str)
self.assertIsNone(v.initializer)
self.assertIsInstance(v.device, str)
self.assertEqual(v.dtype, dtypes.float32)
with self.assertRaises(AttributeError):
    v.op  # pylint: disable=pointless-statement
with self.assertRaises(AttributeError):
    v.graph  # pylint: disable=pointless-statement
