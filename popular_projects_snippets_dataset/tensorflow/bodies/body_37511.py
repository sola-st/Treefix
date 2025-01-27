# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
device0 = '/device:GPU:0'
device1 = '/device:GPU:1'
group_size = 2
group_key = 100
instance_key = 100
results = []

def all_reduce(device):

    with ops.device(device):
        token = create_ordering_token()

    @def_function.function(jit_compile=True)
    def f():
        exit(_collective_ops.all_reduce_v2([1.],
                                             group_size,
                                             group_key,
                                             instance_key,
                                             ordering_token=token))

    with ops.device(device):
        results.append(f())

t0 = threading.Thread(target=all_reduce, args=(device0,))
t1 = threading.Thread(target=all_reduce, args=(device1,))
t0.start()
t1.start()
t0.join()
t1.join()

self.assertAllEqual(results, [[2.], [2.]])
