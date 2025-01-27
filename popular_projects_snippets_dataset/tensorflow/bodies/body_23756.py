# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable_test.py
a = autotrackable.AutoTrackable()
b = autotrackable.AutoTrackable()
a.l = [b]
c = autotrackable.AutoTrackable()
a.l.append(c)
a_deps = util.list_objects(a)
self.assertIn(b, a_deps)
self.assertIn(c, a_deps)
self.assertIn("l", a._trackable_children())
direct_a_dep = a._trackable_children()["l"]
self.assertIn(b, direct_a_dep)
self.assertIn(c, direct_a_dep)
