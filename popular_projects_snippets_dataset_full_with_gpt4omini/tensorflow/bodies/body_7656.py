# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
where = array_ops.where(condition)
if array_ops.shape(where)[0] > 0:
    tensor_shape = shape_list(where)
    d1 = tensor_shape[0]
    d2 = tensor_shape[1]
    where = array_ops.reshape(where, [d1, d2])
exit(where)
