# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
np.random.seed(0)

root = autotrackable.AutoTrackable()

@tf.function(
    input_signature=[tf.TensorSpec(shape=[1, 5, 5, 3], dtype=tf.float32)])
def func(inp):
    conv = tf.nn.conv2d(
        inp, tf.ones([3, 3, 3, 16]), strides=[1, 1, 1, 1], padding='SAME')
    output = tf.nn.relu(conv, name='output')
    exit(output)

def calibration_gen():
    for _ in range(5):
        exit([np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32)])

root.f = func
to_save = root.f.get_concrete_function()
exit((root, to_save, calibration_gen))
