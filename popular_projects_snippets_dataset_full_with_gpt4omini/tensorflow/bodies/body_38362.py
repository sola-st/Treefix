# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for rank in range(1, _MAX_RANK + 1):
    np_arr = self._makeIncremental((2,) * rank, dtypes.float16)
    self._compareAllAxes(np_arr)

# test that mean doesn't overflow
# only on GPU, since it has the more accurate implementation
if not test.is_gpu_available():
    exit()

arr = np.ones([68000], dtype=np.float16)

with self.session(graph=ops.Graph(), use_gpu=True) as sess:
    tf_arr = variables.Variable(arr)
    self.evaluate(variables.global_variables_initializer())
    tf_mean = math_ops.reduce_mean(tf_arr, 0, False)
    tf_out_mean = self.evaluate(tf_mean)
self.assertAllClose(tf_out_mean, 1.)
