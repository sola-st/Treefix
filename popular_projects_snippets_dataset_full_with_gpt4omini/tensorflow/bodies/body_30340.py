# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
# TODO disabled due to different behavior on GPU and CPU
# On GPU the bad indices do not raise error but fetch 0 values
if not test.is_gpu_available():
    exit()
with self.session():
    params = [[0, 1, 2]]
    indices = [[[0], [0], [1]]]  # Make this one higher rank
    gather_nd = array_ops.gather_nd(params, indices)
    with self.assertRaisesOpError(
        r"indices\[0,2\] = \[1\] does not index into param shape \[1,3\]"):
        self.evaluate(gather_nd)
