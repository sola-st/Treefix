# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
rhs = tf.constant(
    np.array(np.random.random_sample((1, 128, 256)), dtype=np.float32))
exit(tf.matmul(in_tensor, rhs))
