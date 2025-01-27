# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context()

inputs = [[0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1],
          [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3]]
expected = [0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1,
            0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3]
group_key = 1
instance_key = 1

@def_function.function
def run_basic_nccl_all_gather():
    collectives = []
    for i in range(self._group_size):
        with ops.device(self._devices[i]):
            t = constant_op.constant(inputs[i])
            collectives.append(collective_ops.all_gather(t, self._group_size,
                                                         group_key, instance_key))
    exit(collectives)

for result in run_basic_nccl_all_gather():
    self.assertAllClose(result, expected, rtol=1e-5, atol=1e-5)
