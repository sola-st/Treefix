# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
x = constant_op.constant(x)
exit(api.copy_to_mesh(
    x, Layout.replicated(self.mesh, rank=x.shape.ndims)))
