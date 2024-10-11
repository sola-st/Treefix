# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
if device == 'GPU' and context.num_gpus() < 4:
    self.skipTest('not enough GPU')

num_elements = 4
tokens = {}
for device_idx in range(num_elements):
    dev = '/{}:{}'.format(device, device_idx)
    with ops.device(dev):
        tokens[dev] = create_ordering_token()

@def_function.function
def run_all_reduce(group_size, group_key):
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

def run_and_assert(group_size, group_key):
    for reduced_tensor in run_all_reduce(group_size, group_key):
        self.assertAllEqual(
            [float(group_key) * group_size for i in range(num_elements)],
            reduced_tensor.numpy())

run_and_assert(group_size=2, group_key=1)
run_and_assert(group_size=3, group_key=2)
