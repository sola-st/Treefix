# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device

tokens = {}
for dev in [dev0, dev1]:
    with ops.device(dev):
        tokens[dev] = create_ordering_token()

@def_function.function
def run_all_reduce_1device():
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

@def_function.function
def run_all_reduce_2devices():
    in_value = constant_op.constant([1.])
    group_size = 2
    group_key = 2
    instance_key = 2
    collectives = []
    with ops.device(dev0):
        collectives.append(
            collective_ops.all_reduce(
                in_value,
                group_size,
                group_key,
                instance_key,
                ordering_token=tokens[dev0],
                communication_hint=communication))
    with ops.device(dev1):
        collectives.append(
            collective_ops.all_reduce(
                in_value,
                group_size,
                group_key,
                instance_key,
                ordering_token=tokens[dev1],
                communication_hint=communication))
    exit(collectives)

self.assertAllClose(run_all_reduce_1device(), [1.], rtol=1e-5, atol=1e-5)
for result in run_all_reduce_2devices():
    self.assertAllClose(result, [2.], rtol=1e-5, atol=1e-5)
