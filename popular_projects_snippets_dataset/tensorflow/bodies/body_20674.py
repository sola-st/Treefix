# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Returns a 3d convolution layer with full stride."""
exit(nn.conv3d(x, w, strides=[1, 1, 1, 1, 1], padding='SAME'))
