# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
a = ExtensionTypeWithTensorDefault()

# Check that the default values were *not* converted to Tensors:
sig = tf_inspect.signature(ExtensionTypeWithTensorDefault.__init__)
self.assertIsInstance(sig.parameters['x'].default, int)
self.assertIsInstance(sig.parameters['y'].default, list)

# The following would fail with "RuntimeError: Attempting to capture an
# EagerTensor without building a function" if we converted the default
# value to a Tensor when we built the type.
self.assertAllEqual(a.x + constant_op.constant(3), 8)
