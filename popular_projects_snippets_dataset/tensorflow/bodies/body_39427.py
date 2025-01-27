# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/trackable_view_test.py
root = base.Trackable()
leaf = base.Trackable()
root._track_trackable(leaf, name="leaf")
(current_name,
 current_dependency), = trackable_view.TrackableView.children(root).items()
self.assertIs(leaf, current_dependency)
self.assertEqual("leaf", current_name)
