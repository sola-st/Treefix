# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
s1 = structure.type_spec_from_value(value1_fn())
s2 = structure.type_spec_from_value(value2_fn())
s3 = structure.type_spec_from_value(value3_fn())
for c1, c2, c3 in zip(nest.flatten(s1), nest.flatten(s2), nest.flatten(s3)):
    self.assertEqual(hash(c1), hash(c1))
    self.assertEqual(hash(c1), hash(c2))
    self.assertNotEqual(hash(c1), hash(c3))
    self.assertNotEqual(hash(c2), hash(c3))
