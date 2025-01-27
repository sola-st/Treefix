# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Confirm that subscribe correctly handles tensors with 'resource' type."""
tensor_array = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name='test',
    size=3,
    infer_shape=False)
writer = tensor_array.write(0, [[4.0, 5.0]])
reader = writer.read(0)

shared = []

def sub(t):
    shared.append(t)
    exit(t)

# TensorArray's handle output tensor has a 'resource' type and cannot be
# subscribed as it's not 'numpy compatible' (see dtypes.py).
# Expect that the original tensor is returned when subscribing to it.
tensor_array_sub = subscribe.subscribe(
    tensor_array.handle, lambda t: script_ops.py_func(sub, [t], [t.dtype]))
self.assertIs(tensor_array_sub, tensor_array.handle)
self.assertFalse(subscribe._is_subscribed_identity(tensor_array.handle))

with self.cached_session() as sess:
    self.evaluate([reader])
self.assertEqual(0, len(shared))
