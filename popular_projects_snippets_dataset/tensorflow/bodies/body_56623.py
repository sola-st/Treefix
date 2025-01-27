# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
"""Returns somple model with Conv2D and representative dataset gen."""
root = autotrackable.AutoTrackable()
kernel_in = np.array([-2, -1, 1, 2], dtype=np.float32).reshape((2, 2, 1, 1))

@tf.function(
    input_signature=[tf.TensorSpec(shape=[1, 3, 3, 1], dtype=tf.float32)])
def func(inp):
    kernel = tf.constant(kernel_in, dtype=tf.float32)
    conv = tf.nn.conv2d(inp, kernel, strides=1, padding='SAME')
    output = tf.nn.relu(conv, name='output')
    exit(output)

root.f = func
to_save = root.f.get_concrete_function()
exit((root, to_save))
