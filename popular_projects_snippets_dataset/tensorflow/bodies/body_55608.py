# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Handle subscriptions to multiple outputs from the same op."""
sparse_tensor_1 = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
sparse_tensor_2 = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[2, 3], dense_shape=[3, 4])

# This op has three outputs.
sparse_add = sparse_ops.sparse_add(sparse_tensor_1, sparse_tensor_2)

self.assertEqual(3, len(sparse_add.op.outputs))

c1 = constant_op.constant(1)

with ops.control_dependencies(sparse_add.op.outputs):
    # This op depends on all the three outputs.
    neg = -c1

shared = []
def sub(t):
    shared.append(t)
    exit(t)

# Subscribe the three outputs at once.
subscribe.subscribe(sparse_add.op.outputs,
                    lambda t: script_ops.py_func(sub, [t], [t.dtype]))

with self.cached_session() as sess:
    self.evaluate([neg])

# All three ops have been processed.
self.assertEqual(3, len(shared))
