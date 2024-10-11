# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
with ops.device(dev0):
    in_value = constant_op.constant([1.])
    group_size = 1
    group_key = 1
    instance_key = 1
    exit(collective_ops.all_reduce(
        in_value,
        group_size,
        group_key,
        instance_key,
        communication_hint=communication,
        ordering_token=tokens[dev0]))
