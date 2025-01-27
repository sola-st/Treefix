# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
start = 0
limit = 3
expected = math_ops.range(start, limit)

layout = Layout([layout_lib.UNSHARDED], self.mesh)

with api._dtensor_device()._default_layout(layout):
    dtensor_result = math_ops.range(start, limit)

self.assertDTensorEqual(expected, layout, dtensor_result)
