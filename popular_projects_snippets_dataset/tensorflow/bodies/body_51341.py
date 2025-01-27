# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
imported = load.load(self._v1_single_metagraph_saved_model(
    use_resource=True))
self.evaluate(variables.global_variables_initializer())
self.evaluate(variables.local_variables_initializer())
fn = imported.signatures["serving_default"]
self.assertEqual({"output": 6.},
                 self.evaluate(fn(constant_op.constant(2.))))
self.assertAllEqual([3., 1.], self.evaluate(imported.variables))
self.evaluate(imported.variables[0].assign(4.))
self.assertEqual({"output": 8.},
                 self.evaluate(fn(start=constant_op.constant(2.))))
self.evaluate(imported.variables[1].assign(2.))
self.assertEqual({"output": 24.},
                 self.evaluate(fn(start=constant_op.constant(3.))))
self.assertTrue(imported.variables[0].trainable)
self.assertFalse(imported.variables[1].trainable)
with backprop.GradientTape() as tape:
    output = fn(start=constant_op.constant(4.))
self.assertEqual(imported.variables[:1], list(tape.watched_variables()))
self.assertEqual(
    8.,
    self.evaluate(tape.gradient(output, imported.variables[0])))
