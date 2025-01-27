# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
self._testBatchNormArbitraryShapes((3, 3), (1, 3), dtype=dtypes.float16,
                                   param_dtype=dtypes.float32, atol=0.001)
