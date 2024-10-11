# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context()

inputs = [[0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1],
          [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3]]
expected = [0.2, 1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2]
group_key = 1
instance_key = 100

@def_function.function
def run_fp16_reduce():
    collectives = []
    for i in range(self._group_size):
        with ops.device(self._devices[i]):
            t = constant_op.constant(inputs[i], dtype=dtypes.float16)
            collectives.append(collective_ops.all_reduce(
                t, self._group_size, group_key, instance_key, 'Add', 'Div'))
    exit(collectives)

for result in run_fp16_reduce():
    self.assertAllClose(result, expected, rtol=1e-3, atol=1e-3)
