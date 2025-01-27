# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[16, 4], dtype=dtypes.float32, name='input1')
    in_tensor_2 = constant_op.constant(
        matrix_b_values, shape=[4, 8], dtype=dtypes.float32)
    out_tensor = math_ops.matmul(in_tensor_1, in_tensor_2)
    sess = session.Session()

exit((sess, [in_tensor_1], [out_tensor]))
