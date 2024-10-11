# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
layout = Layout.replicated(self.mesh, rank=3)
# Due to Perf concerns, `pack` does not check the compatibility of
# components and layout. Here, we inject a wrong value components.
with api.run_on(self.mesh):
    b = api.pack(
        [constant_op.constant([[[(x + 1) * 1.0]]]) for x in range(8)],
        layout=layout)
    assert b.shape == [1, 1, 1]

# `to_numpy` assumes all unpacked tensors are compatible with the
# layout. So, it picks any component to use if that dimension is replicated.
# In this case, it picks the final one.
result_dtensor = numpy_util.to_numpy(b)

self.assertAllEqual(constant_op.constant([[[8.]]]), result_dtensor)

# assertDTensorEqual does more aggressive check, which respects the layout.
with self.assertRaisesRegex(AssertionError, 'Mismatched value'):
    self.assertDTensorEqual(constant_op.constant([[[8.]]]), layout, b)
