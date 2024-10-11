# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(1.0, trainable=True)
root.v2 = variables.Variable(2.0, trainable=False)
self.evaluate([root.v1.initializer, root.v2.initializer])

for _ in range(cycles):
    imported = cycle(root, 1, use_cpp_bindings=use_cpp_bindings)
    self.evaluate([imported.v1.initializer, imported.v2.initializer])

if not context.executing_eagerly():
    self.assertIsInstance(imported.v1.initializer, ops.Operation)
    self.assertIsInstance(imported.v2.initializer, ops.Operation)

self.assertEqual(self.evaluate(imported.v1), 1.0)
self.assertTrue(imported.v1.trainable)
self.assertEqual(self.evaluate(imported.v2), 2.0)
self.assertFalse(imported.v2.trainable)
