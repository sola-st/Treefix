# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
if attr is None:
    self.skipTest("attr module is unavailable.")

field_values = [1, 2]
sample_attr = NestTest.SampleAttr(*field_values)
self.assertFalse(nest._is_attrs(field_values))
self.assertTrue(nest._is_attrs(sample_attr))
flat = nest.flatten(sample_attr)
self.assertEqual(field_values, flat)
restructured_from_flat = nest.pack_sequence_as(sample_attr, flat)
self.assertIsInstance(restructured_from_flat, NestTest.SampleAttr)
self.assertEqual(restructured_from_flat, sample_attr)

# Check that flatten fails if attributes are not iterable
with self.assertRaisesRegex(TypeError, "object is not iterable"):
    flat = nest.flatten(NestTest.BadAttr())
