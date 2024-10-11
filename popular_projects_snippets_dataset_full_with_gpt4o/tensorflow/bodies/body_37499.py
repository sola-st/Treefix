# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
if device == 'GPU' and context.num_gpus() < 4:
    self.skipTest('not enough GPU')

dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device
dev2 = '/device:%s:2' % device
dev3 = '/device:%s:3' % device

tokens = {}
for dev in [dev0, dev1, dev2, dev3]:
    with ops.device(dev):
        tokens[dev] = create_ordering_token()

@def_function.function
def run_all_reduce_4devices_same_instance_key():
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

results = run_all_reduce_4devices_same_instance_key()
self.assertAllClose(results[0], 3., rtol=1e-5, atol=1e-5)
self.assertAllClose(results[1], 3., rtol=1e-5, atol=1e-5)
self.assertAllClose(results[2], 7., rtol=1e-5, atol=1e-5)
self.assertAllClose(results[3], 7., rtol=1e-5, atol=1e-5)
