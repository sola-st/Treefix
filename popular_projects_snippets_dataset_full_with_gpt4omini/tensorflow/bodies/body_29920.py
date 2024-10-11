# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
for use_gpu in (True, False):
    self._testZeroDimReshape(x=np.zeros([0, 6]).astype(np.float32),
                             shape=[0, -1, 3],
                             expected=(0, 2, 3),
                             use_gpu=use_gpu)
