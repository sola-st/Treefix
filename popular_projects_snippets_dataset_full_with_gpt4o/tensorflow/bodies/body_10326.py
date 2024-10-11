# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
config = {
    'shape': [2, 3, 4, 5],
    'err_tolerance': 2e-2,
    'dtype': np.float16,
}
self._testBatchNormGradGrad(config)
