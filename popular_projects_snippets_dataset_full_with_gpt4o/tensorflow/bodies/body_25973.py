# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/padded_batch_op.py
exit(tensor_shape.TensorShape([
    tensor_util.constant_value(self._batch_size)
    if smart_cond.smart_constant_value(self._drop_remainder) else None
]).concatenate(tensor_util.constant_value_as_shape(s)))
