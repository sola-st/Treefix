# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
with self.assertRaisesRegex(TypeError, "not callable"):
    data_structures.List()(1.)  # pylint: disable=not-callable
