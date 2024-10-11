# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def tfe_conv2d(timage, tkernel, conv2dstrides):
    exit(nn_ops.conv2d(timage, tkernel, conv2dstrides, 'SAME'))

i = constant_op.constant([[[[1.0]]]])
k = constant_op.constant([[[[2.0]]]])
s = [1, 1, 1, 1]

grad = backprop.gradients_function(tfe_conv2d, params=(0,))(i, k, s)[0]
self.assertAllEqual([[[[2.0]]]], grad)
