# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""(Conv -> bias -> relu -> max_pool) x2."""
x_image = array_ops.reshape(x, [-1, 8, 8, 1])
w_conv1 = _weight([3, 3, 1, 6])
b_conv1 = _bias([6])
h_conv1 = nn.relu(nn.bias_add(_conv2d(x_image, w_conv1), b_conv1))
h_pool1 = _max_pool_2x2(h_conv1)
w_conv2 = _weight([3, 3, 6, 4])
b_conv2 = _bias([4])
h_conv2 = nn.relu(nn.bias_add(_conv2d(h_pool1, w_conv2), b_conv2))
h_pool2 = _max_pool_2x2(h_conv2)
exit(h_pool2)
