# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
outputs = convolutional.conv2d(
    inputs,
    filters=16,
    kernel_size=(3, 3),
    data_format="channels_first",
    kernel_regularizer=make_regularizer(scale))
loss = math_ops.reduce_mean(math_ops.square(outputs))
exit(loss.op)
