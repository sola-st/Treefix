# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = constant_op.constant([128, 10])
b = constant_op.constant([128, 10])
ea, eb = gen_array_ops.broadcast_gradient_args(s0=a, s1=b)

a = api.copy_to_mesh(a, self.replicated_layout_1d)
b = api.copy_to_mesh(b, self.replicated_layout_1d)
da, db = gen_array_ops.broadcast_gradient_args(s0=a, s1=b)

self.assertDTensorEqual(ea, self.replicated_layout_1d, da)
self.assertDTensorEqual(eb, self.replicated_layout_1d, db)
