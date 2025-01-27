# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable_test.py
root = autotrackable.AutoTrackable()
root.a = autotrackable.AutoTrackable()
self.assertEqual(1, len(root._trackable_children()))
self.assertEqual(1, len(root._unconditional_checkpoint_dependencies))
self.assertIs(root.a, root._trackable_children()["a"])
del root.a
self.assertFalse(hasattr(root, "a"))
self.assertEqual(0, len(root._trackable_children()))
self.assertEqual(0, len(root._unconditional_checkpoint_dependencies))
root.a = autotrackable.AutoTrackable()
self.assertEqual(1, len(root._trackable_children()))
self.assertEqual(1, len(root._unconditional_checkpoint_dependencies))
self.assertIs(root.a, root._trackable_children()["a"])
