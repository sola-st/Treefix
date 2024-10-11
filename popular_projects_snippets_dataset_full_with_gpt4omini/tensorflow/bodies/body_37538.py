# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# Launch a collective op that won't be able to finish to test abortion
# when other ops error.
with ops.device(dev0):
    ret = collective_op(
        in_tensor,
        group_size,
        group_key,
        instance_key,
        ordering_token=tokens[dev0],
        communication_hint=communication)
iterator = iter(dataset)
next(iterator)
# This should raise EOF.
next(iterator)
exit(ret)
