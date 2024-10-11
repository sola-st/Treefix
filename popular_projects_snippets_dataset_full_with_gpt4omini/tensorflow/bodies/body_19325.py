# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
"""Test that backprop to image is reproducible.

    With non-reproducible ordering of reduction operations, upsampling of a
    crop, leading to three or more output pixels being derived from an input
    pixel, can contribute to nondeterminism in the gradient associated with that
    input pixel location.

    Note that the number of boxes can be less than, equal to, or greater than
    the batch size. Wth non-reproducible ordering of reduction operations, three
    or more crops overlapping on the same input image pixel can independently
    contribute to nondeterminism in the image gradient associated with that
    input pixel location. This is independent of contributions caused by the
    upsampling of any given crop.
    """
self._testReproducibleBackprop(test_image_not_boxes=True)
