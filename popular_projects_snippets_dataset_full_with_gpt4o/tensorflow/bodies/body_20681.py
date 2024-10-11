# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Returns a 2d depthwise convolution layer with full stride."""
exit(nn.depthwise_conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME'))
