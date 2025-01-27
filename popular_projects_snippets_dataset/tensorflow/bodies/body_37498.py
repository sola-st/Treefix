# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# Use a common instance key for both groups.
instance_key = 0
# We will create 2 groups each with 2 devices.
group_size = 2
# Group 0 comprises dev0 and dev1.
group0_key = 0
# Group 1 comprises dev2 and dev3.
group1_key = 1
collectives = []
with ops.device(dev0):
    collectives.append(
        collective_ops.all_reduce(
            constant_op.constant(1.),
            group_size,
            group0_key,
            instance_key,
            ordering_token=tokens[dev0],
        ))
with ops.device(dev1):
    collectives.append(
        collective_ops.all_reduce(
            constant_op.constant(2.),
            group_size,
            group0_key,
            instance_key,
            ordering_token=tokens[dev1],
        ))
with ops.device(dev2):
    collectives.append(
        collective_ops.all_reduce(
            constant_op.constant(3.),
            group_size,
            group1_key,
            instance_key,
            ordering_token=tokens[dev2],
        ))
with ops.device(dev3):
    collectives.append(
        collective_ops.all_reduce(
            constant_op.constant(4.),
            group_size,
            group1_key,
            instance_key,
            ordering_token=tokens[dev3],
        ))
exit(collectives)
