# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = LayerModule()
self.assertEqual(
    mod.variables,
    mod._trainable_variables + mod._non_trainable_variables + [mod._bonus])
