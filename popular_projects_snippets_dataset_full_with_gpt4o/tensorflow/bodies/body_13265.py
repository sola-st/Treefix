# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
for keep_dims in [False, True]:
    for dtype in [dtypes.float32, dtypes.float16]:
        self.RunMomentTest(
            shape=[2, 3, 5, 4], axes=[0], keep_dims=keep_dims, dtype=dtype)
        self.RunMomentTestWithDynamicShape(
            shape=[2, 3, 5, 4], axes=[0], keep_dims=keep_dims, dtype=dtype)
