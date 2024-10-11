# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
exit(nn_ops.erosion2d(
    image_tensor,
    kernel_tensor,
    strides=strides,
    rates=rates,
    padding=padding,
    name="erosion2d"))
