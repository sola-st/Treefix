# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
x_image = array_ops.reshape(x, [-1, 28, 28, 1])
w_conv1 = _weight([5, 5, 1, 32])
c_conv1 = _conv2d(x_image, w_conv1)
vector = constant_op.constant(6.4, shape=[32])
add = math_ops.add(c_conv1, vector)
exit(add)
