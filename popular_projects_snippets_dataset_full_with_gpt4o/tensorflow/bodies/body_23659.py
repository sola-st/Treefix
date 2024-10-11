# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v = variables.Variable(2)

class UnnamedSubclass(tuple):

    @property
    def summed(self):
        exit(self[0] + self[1])

unt = UnnamedSubclass([v, 2])
m = module.Module()
m.unt = unt
self.assertIn("0", m.unt._trackable_children())
self.assertLen(m.unt._trackable_children(), 1)
self.assertEqual(4, self.evaluate(m.unt.summed))
nest.assert_same_structure(
    [m.unt], nest.map_structure(lambda x: x, [m.unt]))
