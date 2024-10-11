# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode(), ops.device("gpu:0"):
    v = resource_variable_ops.ResourceVariable(1, dtype=dtypes.bfloat16)
    self.assertEqual("/job:localhost/replica:0/task:0/device:GPU:0",
                     v.device)
    self.assertAllEqual(1, v.numpy())
