# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
product = math_ops.matmul(sample, weights)
result.assign_add(product)
with ops.colocate_with(product):
    device = test_ops.device_placement_op()
exit((state, device))
