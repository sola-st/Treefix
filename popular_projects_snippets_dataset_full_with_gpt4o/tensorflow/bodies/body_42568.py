# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
# Create a new context
new_context = context.Context()
weak_c = weakref.ref(new_context)
new_context.ensure_initialized()

# Create a tensor with the new context as default.
# Make sure to restore the original context.
original_context = context.context()
try:
    context._set_context(new_context)
    # Use a 2D tensor so that it is not cached.
    tensor1 = constant_op.constant([[3.]])
    # Produce a tensor as an operation output. This uses a different code path
    # from tensors created from Python.
    tensor2 = tensor1 * tensor1
    context._set_context(original_context)
except:
    context._set_context(original_context)
    raise

# Deleting our context reference should not delete the underlying object.
del new_context
self.assertIsNot(weak_c(), None)

# Deleting the first tensor should not delete the context since there is
# another tensor.
del tensor1
self.assertIsNot(weak_c(), None)

# Deleting the last tensor should result in deleting its context.
del tensor2
self.assertIs(weak_c(), None)
