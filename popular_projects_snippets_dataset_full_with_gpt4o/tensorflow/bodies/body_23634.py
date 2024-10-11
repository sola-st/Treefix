# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
original = autotrackable.AutoTrackable()
original_sub = autotrackable.AutoTrackable()
original.a = [[1.]]
original.b = {"a": original_sub}
shallow_copied = copy.copy(original)
self.assertIs(original_sub, shallow_copied.b["a"])
self.assertIsNot(original, shallow_copied)
self.assertEqual([[1.]], shallow_copied.a)
shallow_deps = util.list_objects(shallow_copied)
self.assertIn(shallow_copied.a, shallow_deps)
self.assertIn(shallow_copied.b, shallow_deps)
self.assertIn(shallow_copied.b["a"], shallow_deps)
