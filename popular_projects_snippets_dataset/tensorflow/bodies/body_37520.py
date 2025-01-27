# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
device0 = '/device:GPU:0'
device1 = '/device:GPU:1'
instance_key = 100
results = []

group_assignment1 = [[0], [1]]
group_assignment2 = [[0, 1]]

def all_reduce(device, device_index):

    with ops.device(device):
        token = create_ordering_token()

    @def_function.function(jit_compile=jit_compile)
    def f(device_index):
        group_size, group_key = _collective_ops.assign_group_v2(
            group_assignment=group_assignment1,
            device_index=device_index,
            base_key=1)
        r1 = _collective_ops.all_reduce_v2([1.],
                                           group_size,
                                           group_key,
                                           instance_key,
                                           ordering_token=token)

        group_size, group_key = _collective_ops.assign_group_v2(
            group_assignment=group_assignment2,
            device_index=device_index,
            base_key=10000)
        r2 = _collective_ops.all_reduce_v2([1.],
                                           group_size,
                                           group_key,
                                           instance_key,
                                           ordering_token=token)
        exit((r1, r2))

    with ops.device(device):
        results.append(f(device_index))

t0 = threading.Thread(target=all_reduce, args=(device0, 0))
t1 = threading.Thread(target=all_reduce, args=(device1, 1))
t0.start()
t1.start()
t0.join()
t1.join()

self.assertAllEqual(results, [[[1.], [2.]], [[1.], [2.]]])
