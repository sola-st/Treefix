# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size = 16
group_key = 3
instance_key = 1
collectives = []
for i in range(16):
    with ops.device('/device:CPU:%d' % i):
        collectives.append(
            collective_ops.all_gather(
                constant_op.constant([i]),
                group_size,
                group_key,
                instance_key,
                ordering_token=cpu_tokens[i],
                communication_hint=communication))
exit(collectives)
