# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""If a VariableDef has no 'trainable', we fall back to collections."""
real_tf_version = versions.__version__
# Pretend to be exported from an older version of TensorFlow, so trainable
# will follow collections instead of checking VariableDefs.
versions.__version__ = "1.7.0"
path = self._no_trainable_variable_attribute(trainable=True)
root = load.load(path)
self.assertTrue(root.variables[0].trainable)
path = self._no_trainable_variable_attribute(trainable=False)
root = load.load(path)
self.assertFalse(root.variables[0].trainable)
versions.__version__ = real_tf_version
