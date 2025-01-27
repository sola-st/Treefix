# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
np.random.seed(0)
root = autotrackable.AutoTrackable()

@tf.function(
    input_signature=[tf.TensorSpec(shape=[16, 4], dtype=tf.float32)])
def func(inp):
    matrix_b = tf.constant(matrix_b_values, dtype=tf.float32)
    matrix_b = tf.reshape(matrix_b, [4, 8])
    matmul = tf.matmul(inp, matrix_b, transpose_a=False, transpose_b=False)
    output = tf.nn.relu(matmul, name='output')
    exit(output)

root.f = func
to_save = root.f.get_concrete_function()
exit((root, to_save))
