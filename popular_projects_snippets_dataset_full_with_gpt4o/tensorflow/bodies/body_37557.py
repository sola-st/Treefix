# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device
group_size = 2
group_key = 100
instance_key = 100
in_tensor = constant_op.constant([1.])

with ops.device(dev0):
    token0 = create_ordering_token()
with ops.device(dev1):
    token1 = create_ordering_token()

@def_function.function
def f():
    # Launch the first collective with token.
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=token0,
            name='FirstChainedDev0')
    with ops.device(dev1):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=token1,
            name='FirstChainedDev1')
    # Launch the second collective without token.
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=create_ordering_token(),
            name='UnchainedDev0')
    with ops.device(dev1):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=create_ordering_token(),
            name='UnchainedDev1')
    # Launch the third collective with token.
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key + 1,
            ordering_token=token0,
            name='SecondChainedDev0')
    with ops.device(dev1):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key + 1,
            ordering_token=token1,
            name='SecondChainedDev1')

graph = f.get_concrete_function().graph
for device, suffix in [(dev0, 'Dev0'), (dev1, 'Dev1')]:

    first = graph.get_operation_by_name('FirstChained' + suffix)
    second = graph.get_operation_by_name('Unchained' + suffix)
    third = graph.get_operation_by_name('SecondChained' + suffix)
    self.assertIsNotNone(first)
    self.assertTrue(first.device.endswith(device))
    self.assertIsNotNone(second)
    self.assertTrue(second.device.endswith(device))
    self.assertIsNotNone(third)
    self.assertTrue(third.device.endswith(device))

    # Try to find the third collective, which should have the first collective
    # as a control input.
    self.assertLen(third.control_inputs, 1)
    self.assertEqual(third.control_inputs[0].name, 'FirstChained' + suffix)

    self.assertEmpty(second.control_inputs)
    self.assertEmpty(first.control_inputs)
