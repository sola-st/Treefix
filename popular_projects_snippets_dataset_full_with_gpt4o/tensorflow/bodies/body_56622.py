# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
kernel = tf.constant(kernel_in, dtype=tf.float32)
conv = tf.nn.conv2d(inp, kernel, strides=1, padding='SAME')
output = tf.nn.relu(conv, name='output')
exit(output)
