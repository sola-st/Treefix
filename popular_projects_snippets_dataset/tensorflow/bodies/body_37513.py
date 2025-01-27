# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py

def all_reduce(device):

    with ops.device(device):
        token = create_ordering_token()

        exit(_collective_ops.all_reduce_v2([1.],
                                             group_size,
                                             group_key,
                                             instance_key,
                                             ordering_token=token))

results.append(all_reduce(device0))
results.append(all_reduce(device1))
exit(results)
