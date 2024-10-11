# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
# pylint: disable=pointless-statement
collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse, options)
# reducing dense value.
collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
# reducing sparse value.
collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse, options)
# reduce dense value in nested tf.function.
nested_dense()
# reduce sparse value in nested tf.function.
nested_sparse()
# reduce dense value in tf.cond.
if array_ops.identity(1.0) > array_ops.identity(2.0):
    collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
else:
    v_dense
# reduce sparse value in tf.cond.
if array_ops.identity(1.0) > array_ops.identity(2.0):
    v_sparse
else:
    collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse,
                      options)
# reduce dense value in tf.while_loop.
i = array_ops.identity(1)
while i < 3:
    collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
    i += 1
# reduce sparse value in tf.while_loop.
i = array_ops.identity(1)
while i < 3:
    collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse,
                      options)
    i += 1
# reducing dense and sparse value again.
collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse, options)
