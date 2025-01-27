# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
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
