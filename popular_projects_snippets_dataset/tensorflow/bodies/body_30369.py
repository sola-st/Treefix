# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
# TODO disabled due to different behavior on GPU and CPU
# On GPU the bad indices do not raise error but fetch 0 values
if not test.is_gpu_available():
    exit()
with self.session():
    params = [[0, 1, 2], [3, 4, 5]]
    with self.assertRaisesOpError(r"indices\[0,0\] = 7 is not in \[0, 2\)"):
        array_ops.gather(params, [[7]], axis=0).eval()
    with self.assertRaisesOpError(r"indices\[0,0\] = 7 is not in \[0, 3\)"):
        array_ops.gather(params, [[7]], axis=1).eval()
