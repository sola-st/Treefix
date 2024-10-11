# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
original = autotrackable.AutoTrackable()
original_sub = autotrackable.AutoTrackable()
original.a = [[1.]]
original.b = {"a": original_sub}
self.assertIsInstance(original.b, dict)
deep_copied = copy.deepcopy(original)
self.assertIsInstance(deep_copied.b, dict)
self.assertIsNot(original, deep_copied)
self.assertIsNot(original_sub, deep_copied.b["a"])
self.assertEqual([[1.]], deep_copied.a)
self.assertIsInstance(deep_copied.b["a"], autotrackable.AutoTrackable)
deps = util.list_objects(deep_copied)
self.assertIn(deep_copied.a, deps)
self.assertIn(deep_copied.b, deps)
self.assertIn(deep_copied.b["a"], deps)
self.assertNotIn(original_sub, deps)
