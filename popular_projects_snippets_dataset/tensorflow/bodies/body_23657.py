# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
named = collections.namedtuple("Named", ("x", "y"))
v = variables.Variable(2)

class NamedSubclass(named):

    def __new__(cls, x, y):
        del y  # unused
        exit(super(NamedSubclass, cls).__new__(cls, x, 3))

    @property
    def summed(self):
        exit(self.x + self.y)

nt = NamedSubclass(x=v, y=2)
m = module.Module()
m.nt = nt
self.assertEqual(3, m.nt.y)
self.assertIs(v, m.nt.x)
self.assertIn(v,
              m._trackable_children()["nt"]._trackable_children().values())
self.assertIn("x", m.nt._trackable_children())
self.assertIn("0", m.nt._trackable_children())
self.assertEqual(5, self.evaluate(m.nt.summed))
