# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
if context.num_gpus() < 2:
    self.skipTest("Need at least 2 GPUs for this test, found %d" %
                  context.num_gpus())
with ops.device("gpu:0"):
    t = constant_op.constant([1.0, 2.0, 3.0])
    inner_l = list_ops.tensor_list_from_tensor(t, element_shape=[])
    outer_l = list_ops.empty_tensor_list(
        element_dtype=dtypes.variant, element_shape=[])
    outer_l = list_ops.tensor_list_push_back(outer_l, inner_l)

# Stress test.
for _ in range(1024):
    with ops.device("gpu:1"):
        outer_l = array_ops.identity(outer_l)
    with ops.device("gpu:0"):
        outer_l = array_ops.identity(outer_l)

with ops.device("gpu:1"):
    _, inner_l = list_ops.tensor_list_pop_back(
        outer_l, element_dtype=dtypes.variant)
    t = list_ops.tensor_list_stack(inner_l, element_dtype=dtypes.float32)
    self.assertAllEqual(t, [1.0, 2.0, 3.0])
