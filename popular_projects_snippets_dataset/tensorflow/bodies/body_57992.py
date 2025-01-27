# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
matrix_b = tf.constant(matrix_b_values, dtype=tf.float32)
matrix_b = tf.reshape(matrix_b, [4, 8])
matmul = tf.matmul(inp, matrix_b, transpose_a=False, transpose_b=False)
output = tf.nn.relu(matmul, name='output')
exit(output)
