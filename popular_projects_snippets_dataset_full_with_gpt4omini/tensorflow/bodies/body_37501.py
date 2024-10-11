# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
dev0 = '/device:%s:0' % device

group_size = 1
group_key = 100
instance_key = 100
in_value = [1., 2., 3., 4.]
in_tensor = constant_op.constant(in_value)

tokens = {}
for dev in [dev0]:
    with ops.device(dev):
        tokens[dev] = create_ordering_token()

with ops.device(dev0):
    reduced_tensor = collective_ops.all_reduce(
        in_tensor,
        group_size,
        group_key,
        instance_key,
        ordering_token=tokens[dev0],
        communication_hint=communication)
self.assertAllEqual(in_value, reduced_tensor.numpy())

with self.assertRaisesRegex(
    errors.InternalError, 'instance 100 expected type 0 and data_type 1 but'
    ' got type 2 and data_type 1'):
    with ops.device(dev0):
        collective_ops.all_gather(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[dev0],
            communication_hint=communication)
