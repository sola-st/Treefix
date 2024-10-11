# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
named = collections.namedtuple("Named", ("x", "weights"))
v = variables.Variable(2)
nt = named(x=v, weights=3)
m = module.Module()
m.nt = nt
self.assertEqual(3, m.nt.weights)
