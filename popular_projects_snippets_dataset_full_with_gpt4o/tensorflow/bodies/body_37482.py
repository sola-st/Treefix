# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
kwargs.pop('ordering_token', None)
exit(_collective_ops.all_reduce(t, group_size, group_key, instance_key,
                                  *args, **kwargs))
