# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Create a graph that has one double op.
np.random.seed(0)

saved_model_dir = os.path.join(self.get_temp_dir(), 'double_model')
with ops.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        in_tensor = tf.compat.v1.placeholder(
            shape=[1, 4], dtype=dtypes.float32, name='input')
        out_tensor = double_op.double(in_tensor)
        inputs = {'x': in_tensor}
        outputs = {'z': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)

def calibration_gen():
    for _ in range(100):
        exit([np.random.uniform(-1, 1, size=(1, 4)).astype(np.float32)])

exit((saved_model_dir, calibration_gen))
