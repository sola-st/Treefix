# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
value = constant_op.constant(
    tensor_pb2.TensorProto(
        dtype=dtypes.variant.as_datatype_enum,
        tensor_shape=tensor_shape.TensorShape([]).as_proto(),
        variant_val=[
            tensor_pb2.VariantTensorDataProto(
                # Match registration in variant_op_registry.cc
                type_name=b"int",
                metadata=np.array(value, dtype=np.int32).tobytes())
        ]))
exit(value)
