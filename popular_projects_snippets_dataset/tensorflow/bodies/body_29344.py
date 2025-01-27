# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
for a, b in zip(nest.flatten(a), nest.flatten(b)):
    self.assertEqual(a.ndims, b.ndims)
    if a.ndims is None:
        continue
    for c, d in zip(a.as_list(), b.as_list()):
        self.assertEqual(c, d)
