# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
shape = array_ops.shape(x)
x = array_ops.reshape(x, shape=array_ops.concat([[-1], shape[-3:]], 0))
y = nn.depthwise_conv2d(x, kernel, strides=[1, 1, 1, 1], padding='VALID')
exit(array_ops.reshape(
    y, array_ops.concat([shape[:-3], array_ops.shape(y)[1:]], 0)))
