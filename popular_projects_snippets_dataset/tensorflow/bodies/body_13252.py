# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
"""Test for a variety of shapes and moments.

    Batch normalization is expected to work regardless of the position and
    dimensionality of the 'depth' axis/axes.
    """
self._testBatchNormArbitraryShapes((3, 3), (1, 3))
self._testBatchNormArbitraryShapes((3, 3), (3, 1))
self._testBatchNormArbitraryShapes((3, 2, 4, 5), (1, 2, 1, 1))
self._testBatchNormArbitraryShapes(
    (2, 3, 2, 4, 5), (1, 1, 1, 4, 5), atol=0.005)
