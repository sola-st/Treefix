# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
nt_type = collections.namedtuple("A", ["x", "y"])
proxied = wrapt.ObjectProxy(nt_type(1, 2))
proxied_spec = structure.type_spec_from_value(proxied)
self.assertEqual(
    structure.type_spec_from_value(nt_type(1, 2)), proxied_spec)
