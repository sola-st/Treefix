# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
t = (variables.Variable(1.),)
m = module.Module()
m.t = t
nest.assert_same_structure(t, m.t)
nest.assert_same_structure(m.t, t)

nt_type = collections.namedtuple("nt", ["x", "y"])
nt = nt_type(x=1, y=2)
m.nt = nt
nest.assert_same_structure(m.nt, nt)
with self.assertRaises(TypeError):  # pylint: disable=g-error-prone-assert-raises
    nest.assert_same_structure(m.nt, m.t)
