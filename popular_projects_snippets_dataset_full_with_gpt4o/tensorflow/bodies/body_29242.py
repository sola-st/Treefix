# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
# pylint: disable=g-generic-assert
not_equal_value_fns = not_equal_value_fns._obj
s1 = structure.type_spec_from_value(value1_fn())
s2 = structure.type_spec_from_value(value2_fn())
self.assertEqual(s1, s1)  # check __eq__ operator.
self.assertEqual(s1, s2)  # check __eq__ operator.
self.assertFalse(s1 != s1)  # check __ne__ operator.
self.assertFalse(s1 != s2)  # check __ne__ operator.
for c1, c2 in zip(nest.flatten(s1), nest.flatten(s2)):
    self.assertEqual(hash(c1), hash(c1))
    self.assertEqual(hash(c1), hash(c2))
for value_fn in not_equal_value_fns:
    s3 = structure.type_spec_from_value(value_fn())
    self.assertNotEqual(s1, s3)  # check __ne__ operator.
    self.assertNotEqual(s2, s3)  # check __ne__ operator.
    self.assertFalse(s1 == s3)  # check __eq_ operator.
    self.assertFalse(s2 == s3)  # check __eq_ operator.
