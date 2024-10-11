# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py

with ops.device(device):
    token = create_ordering_token()

    exit(_collective_ops.all_reduce_v2([1.],
                                         group_size,
                                         group_key,
                                         instance_key,
                                         ordering_token=token))
