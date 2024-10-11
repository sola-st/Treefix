# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""If a VariableDef has a trainable property, we do not use collections."""
path = self._export_variable(
    trainable=True,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES])
root = load.load(path)
self.assertTrue(root.variables[0].trainable)
path = self._export_variable(
    trainable=False,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES,
                 ops.GraphKeys.TRAINABLE_VARIABLES])
root = load.load(path)
self.assertFalse(root.variables[0].trainable)
