# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
if not test.is_gpu_available(cuda_only=True):
    exit()
for outer_dim, ratio, inner_dim, dtype in itertools.product(*self.options):
    op_functor = self.op_functors[1]
    with ops.Graph().as_default():
        self._runGraph(op_functor, outer_dim, ratio, inner_dim, dtype)
