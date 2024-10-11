# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
matrix = array_ops.placeholder(dtypes_lib.int32, shape=[None, None])
result = array_ops.matrix_diag_part(matrix, k=-1)
input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
with self.session():
    result_eval = result.eval(feed_dict={matrix: input_matrix})
self.assertAllEqual([4, 8], result_eval)
