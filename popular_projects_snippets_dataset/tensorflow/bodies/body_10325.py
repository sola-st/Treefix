# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
config = {
    'shape': [2, 3, 2, 2],
    'err_tolerance': 1e-3,
    'dtype': np.float32,
}
self._testBatchNormGradGrad(config)
