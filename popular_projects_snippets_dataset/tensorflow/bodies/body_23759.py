# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable_test.py
a = autotrackable.AutoTrackable()
a.l = []
b = autotrackable.AutoTrackable()
a.l.append([b])
c = autotrackable.AutoTrackable()
a.l[0].append(c)
a_deps = util.list_objects(a)
self.assertIn(b, a_deps)
self.assertIn(c, a_deps)
a.l[0].append(1)
d = autotrackable.AutoTrackable()
a.l[0].append(d)
a_deps = util.list_objects(a)
self.assertIn(d, a_deps)
self.assertIn(b, a_deps)
self.assertIn(c, a_deps)
self.assertNotIn(1, a_deps)
e = autotrackable.AutoTrackable()
f = autotrackable.AutoTrackable()
a.l1 = [[], [e]]
a.l1[0].append(f)
a_deps = util.list_objects(a)
self.assertIn(e, a_deps)
self.assertIn(f, a_deps)
checkpoint = util.Checkpoint(a=a)
checkpoint.save(os.path.join(self.get_temp_dir(), "ckpt"))
a.l[0].append(data_structures.NoDependency([]))
a.l[0][-1].append(5)
checkpoint.save(os.path.join(self.get_temp_dir(), "ckpt"))
# Dirtying the inner list means the root object is unsaveable.
a.l[0][1] = 2
with self.assertRaisesRegex(ValueError, "A list element was replaced"):
    checkpoint.save(os.path.join(self.get_temp_dir(), "ckpt"))
