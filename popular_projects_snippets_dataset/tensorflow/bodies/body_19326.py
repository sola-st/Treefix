# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
"""Test that backprop to boxes is reproducible.

    If the input and output dimensions are the same, then the boxes gradients
    will be deterministically zero. Otherwise, in the presence of
    non-reproducible ordering of reduction operations, nondeterminism can be
    introduced, whether there is upsampling or downsampling and whether or not
    there are overlapping crops.
    """
self._testReproducibleBackprop(test_image_not_boxes=False)
