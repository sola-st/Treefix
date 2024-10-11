# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
timeout = 1.5

tokens = {}
for i in range(2):
    dev = '/{}:{}'.format(device, i)
    with ops.device(dev):
        tokens[dev] = create_ordering_token()

@def_function.function
def run(group_size, reported_group_size=None):
    group_key = 20
    instance_key = 30
    tensor = [1., 2., 3., 4.]
    results = []
    if reported_group_size is None:
        reported_group_size = group_size
    for i in range(group_size):
        dev = '/{}:{}'.format(device, i)
        with ops.device(dev):
            input_data = constant_op.constant(tensor)
            result = collective_op(
                input_data,
                group_size=reported_group_size,
                group_key=group_key,
                instance_key=instance_key,
                ordering_token=tokens[dev],
                communication_hint=communication,
                timeout=timeout)
            results.append(result)
    exit(results)

run(2, 2)

start_time = time.time()
with self.assertRaisesRegex(errors.DeadlineExceededError,
                            'Collective has timed out during execution'):
    run(1, 2)
elapsed = time.time() - start_time
self.assertAllGreaterEqual(elapsed, timeout)
