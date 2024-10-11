# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
with api._dtensor_device()._default_layout(layout):
    exit(constant_op.constant(src_numpy, dtype=dtypes.float32))  # 4x12
