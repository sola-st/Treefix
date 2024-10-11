# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
"""Downsamples a feature map by 2X."""
exit(nn.max_pool(
    x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME'))
