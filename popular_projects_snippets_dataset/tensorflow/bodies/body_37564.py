# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
dev0 = '/device:%s:0' % device
group_size = 2
group_key = [100]
instance_key = 100
in_tensor = constant_op.constant([1.])

with self.assertRaises(errors.InvalidArgumentError):
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=create_ordering_token(),
            communication_hint=communication)
