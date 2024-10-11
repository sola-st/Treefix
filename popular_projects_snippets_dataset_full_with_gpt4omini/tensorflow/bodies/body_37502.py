# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
instance_key = group_key
input_value = [float(group_key) for i in range(num_elements)]
collectives = []
for device_idx in range(group_size):
    dev = '/{}:{}'.format(device, device_idx)
    with ops.device(dev):
        input_tensor = constant_op.constant(input_value)
        collectives.append(
            collective_ops.all_reduce(
                input_tensor,
                group_size,
                group_key,
                instance_key,
                ordering_token=tokens[dev],
                communication_hint=communication))
exit(collectives)
