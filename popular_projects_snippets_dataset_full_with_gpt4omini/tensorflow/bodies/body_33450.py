# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
num_rows_ph = array_ops.placeholder(dtypes.int32)
base_operator = linalg.LinearOperatorIdentity(num_rows=num_rows_ph)

u_shape_ph = array_ops.placeholder(dtypes.int32)
u = array_ops.ones(shape=u_shape_ph)

v_shape_ph = array_ops.placeholder(dtypes.int32)
v = array_ops.ones(shape=v_shape_ph)

diag_shape_ph = array_ops.placeholder(dtypes.int32)
diag_update = array_ops.ones(shape=diag_shape_ph)

operator = linalg.LinearOperatorLowRankUpdate(base_operator,
                                              u=u,
                                              diag_update=diag_update,
                                              v=v)

feed_dict = {
    num_rows_ph: 3,
    u_shape_ph: [1, 1, 2, 3, 2],  # batch_shape = [1, 1, 2]
    v_shape_ph: [1, 2, 1, 3, 2],  # batch_shape = [1, 2, 1]
    diag_shape_ph: [2, 1, 1, 2]  # batch_shape = [2, 1, 1]
}

with self.cached_session():
    shape_tensor = operator.shape_tensor().eval(feed_dict=feed_dict)
    self.assertAllEqual([2, 2, 2, 3, 3], shape_tensor)
    dense = operator.to_dense().eval(feed_dict=feed_dict)
    self.assertAllEqual([2, 2, 2, 3, 3], dense.shape)
