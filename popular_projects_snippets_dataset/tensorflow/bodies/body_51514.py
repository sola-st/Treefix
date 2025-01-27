# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = self._make_model_with_tables()
imported = cycle(root, cycles, signatures={})
keys = constant_op.constant(["brain", "test", "foo", "surgery"])
self.assertAllEqual([0, -1, -1, 2], imported.lookup1(keys).numpy())
self.assertAllEqual([2, 0, 1, -1], imported.lookup2(keys).numpy())
