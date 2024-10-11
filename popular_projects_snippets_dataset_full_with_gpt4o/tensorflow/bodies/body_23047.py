# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/const_broadcast_test.py
"""Return the expected graph to convert."""
dtype = x.dtype
filt1 = constant_op.constant(
    0.3, shape=(3, 3, 2, 1), dtype=dtype, name='filt1')
y1 = nn.conv2d(x, filt1, strides=[1, 1, 1, 1], padding='SAME', name='y1')
z1 = nn.relu(y1, name='z1')
filt2 = constant_op.constant(
    0.3, shape=(3, 3, 1, 1), dtype=dtype, name='filt2')
y2 = nn.conv2d(z1, filt2, strides=[1, 1, 1, 1], padding='SAME', name='y2')
z2 = nn.relu(y2, name='z')
filt3 = constant_op.constant(
    0.3, shape=(3, 3, 1, 1), dtype=dtype, name='filt3')
y3 = nn.conv2d(z2, filt3, strides=[1, 1, 1, 1], padding='SAME', name='y3')
exit(nn.relu(y3, name='output_0'))
