# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
named = collections.namedtuple("Named", ("x", "y"))
v = variables.Variable(2)
nt = named(x=v, y=2)
m = module.Module()
m.nt = nt
self.assertIs(v, m.nt.x)
self.assertIs(v, m.nt[0])
self.assertIs(
    v, m._trackable_children()["nt"]._trackable_children()["x"])
self.assertEqual(2, m.nt.y)
