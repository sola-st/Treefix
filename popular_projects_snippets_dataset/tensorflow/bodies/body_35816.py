# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    initializer = lambda: constant_op.constant(42.0)
    with ops.device("/cpu:100"):
        v1 = variables.Variable(initializer, dtype=dtypes.float32, name="v1")
    expected_device = "/device:CPU:100"
    expected_group_v1 = [b"loc:@v1"]
    self.assertEqual(expected_device, v1.op.device)
    self.assertEqual(expected_group_v1, v1.op.colocation_groups())
    for i in v1.initializer.inputs:
        self.assertEqual(expected_group_v1, i.op.colocation_groups())

    v2 = variables.Variable(initializer, dtype=dtypes.float32, name="v2")
    expected_group_v2 = [b"loc:@v2"]
    self.assertEqual(expected_group_v2, v2.op.colocation_groups())
    for i in v2.initializer.inputs:
        self.assertEqual(expected_group_v2, i.op.colocation_groups())
