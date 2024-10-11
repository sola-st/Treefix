# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
in_value = constant_op.constant([1.])
group_size = 2
group_key = 2
instance_key = 2
collectives = []
with ops.device(dev0):
    collectives.append(
        collective_ops.all_gather(
            in_value,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[dev0],
            communication_hint=communication))
with ops.device(dev1):
    collectives.append(
        collective_ops.all_gather(
            in_value,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[dev1],
            communication_hint=communication))
exit(collectives)
