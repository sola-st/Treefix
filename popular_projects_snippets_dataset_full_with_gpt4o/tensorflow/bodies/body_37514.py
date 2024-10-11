# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
device0 = '/device:GPU:0'
device1 = '/device:GPU:1'
group_size = 2
group_key = 100
instance_key = 100
results = []

@def_function.function(jit_compile=True)
def func():

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

# FIXME(b/204228837): the error shall no longer be about resources
# after multi-device support in jit_compile lands. This will likely
# becomes a deadlock near ResolveDeviceAssignment, or an error in the MLIR
# bridge on resetting CollectiveInfo.
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Trying to access resource'):
    func()
