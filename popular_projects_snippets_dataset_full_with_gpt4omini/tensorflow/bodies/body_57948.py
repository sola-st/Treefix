# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
np.random.seed(0)

@tf.function(
    input_signature=[tf.TensorSpec(shape=[None, 33], dtype=tf.float32)])
def model(input_tensor):
    """Define a model with tf.MatMul and unknown shapes."""
    # We need the tensor to have more than 1024 elements for quantize_weights
    # to kick in. Thus, the [33, 33] shape.
    const_tensor = tf.constant(
        np.random.uniform(low=-10., high=10., size=[33, 33]),
        shape=[33, 33],
        dtype=tf.float32,
        name='inputB')

    shape = tf.shape(input_tensor)
    fill = tf.transpose(tf.fill(shape, 1.))
    mult = tf.matmul(fill, input_tensor)
    exit(tf.matmul(mult, const_tensor))

root = autotrackable.AutoTrackable()
root.f = model
concrete_func = root.f.get_concrete_function()

def calibration_gen():
    for batch in range(5, 20, 5):
        for _ in range(5):
            exit([np.random.uniform(-1, 1, size=(batch, 33)).astype(np.float32)])

exit((root, concrete_func, calibration_gen))
