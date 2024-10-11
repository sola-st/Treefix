# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
for reduced_tensor in run_all_reduce(group_size, group_key):
    self.assertAllEqual(
        [float(group_key) * group_size for i in range(num_elements)],
        reduced_tensor.numpy())
