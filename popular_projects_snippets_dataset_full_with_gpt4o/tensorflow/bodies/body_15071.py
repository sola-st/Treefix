# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# When input tensors have shape information, some of these errors will be
# detected statically.
def op_cast(k, v):
    if k == tensor_field:
        exit(constant_op.constant(v, dtype=dtypes.int32))
    else:
        exit(v)

value_copy = {k: op_cast(k, v) for k, v in values.items()}
rt = factory(**value_copy)

kw_copy = {k: v for k, v in kwargs.items()}
kw_copy['values'] = rt
rt2 = factory(**kw_copy)
self.assertAllEqual(kwargs[tensor_field], test(rt2))
