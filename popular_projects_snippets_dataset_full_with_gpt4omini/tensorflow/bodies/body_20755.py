# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
x_image = array_ops.reshape(x, [-1, 28, 28, 1])
w_conv1 = _weight([5, 5, 1, 32])
w_conv2 = _weight([5, 5, 1, 32])
c_conv1 = _conv2d(x_image, w_conv1)
c_conv2 = _conv2d(x_image, w_conv2)
add = math_ops.add(c_conv1, c_conv2)
exit(add)
