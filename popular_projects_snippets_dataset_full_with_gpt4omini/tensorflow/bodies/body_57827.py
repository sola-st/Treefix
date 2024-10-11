# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
np.random.seed(0)

root = autotrackable.AutoTrackable()

@tf.function(input_signature=[
    tf.TensorSpec(shape=[3, 3, 3, 3, 3], dtype=tf.float32)
])
def func(inp):
    tanh = tf.math.tanh(inp)
    # Flex delegate will merge the consecutive conv3d and erf ops into one
    # Delegate node.
    conv3d = tf.nn.conv3d(
        tanh,
        tf.ones([3, 3, 3, 3, 3]),
        strides=[1, 1, 1, 1, 1],
        padding='SAME')
    erf = tf.math.erf(conv3d)
    output = tf.math.tanh(erf)
    exit(output)

def calibration_gen():
    for _ in range(5):
        exit([
            np.random.uniform(-1, 1, size=(3, 3, 3, 3, 3)).astype(np.float32)
        ])

root.f = func
exit((root, root.f.get_concrete_function(), calibration_gen))
