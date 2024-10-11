# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/trackable_view_test.py
root = base.Trackable()
leaf = base.Trackable()
root._track_trackable(leaf, name="leaf")
descendants = trackable_view.TrackableView(root).descendants()
self.assertIs(2, len(descendants))
self.assertIs(root, descendants[0])
self.assertIs(leaf, descendants[1])
