# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
np.random.seed(0)

root = autotrackable.AutoTrackable()

@tf.function(input_signature=[
    tf.TensorSpec(shape=[3], dtype=tf.float32),
    tf.TensorSpec(shape=[3], dtype=tf.float32)
])
def func(a, b):
    # ceil kernel does not support int8 nor int16 types neither.
    left = tf.math.ceil(a)
    right = tf.nn.tanh(b)
    add = tf.math.add(left, right)
    # ceil kernel does not support int8 nor int16 types neither.
    output = tf.math.ceil(add)
    exit((output, right))

def calibration_gen():
    for _ in range(5):
        exit([
            np.random.uniform(-1, 1, size=(3)).astype(np.float32),
            np.random.uniform(-1, 1, size=(3)).astype(np.float32)
        ])

root.f = func
exit((root, root.f.get_concrete_function(), calibration_gen))
