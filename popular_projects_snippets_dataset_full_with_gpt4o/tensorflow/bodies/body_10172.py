# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
ta = tensor_array_ops.TensorArray(dtypes.int32, size=1)
h = math_ops.cast(ta.flow, dtypes.variant)

t = full_type_pb2.FullTypeDef(
    type_id=full_type_pb2.TFT_PRODUCT,
    args=[full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_ARRAY)])
h.op.experimental_set_type(t)

ta = tensor_array_ops.TensorArray(dtypes.int32, flow=h)
ta = ta.write(0, constant_op.constant(1))
exit(ta.stack())
