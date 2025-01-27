# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
if attr is None:
    self.skipTest("attr module is unavailable.")

structure = NestTest.UnsortedSampleAttr(*values)
new_structure = nest.map_structure(lambda x: x, structure)
self.assertEqual(structure, new_structure)
