# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
# TODO(ebrevdo): Re-enable use_gpu=True once non-DMA Variant
# copying between CPU and GPU is supported AND we register a
# ZerosLike callback for GPU for Variant storing primitive types
# in variant_op_registry.cc.
with self.session(use_gpu=False):
    variant_tensor = tensor_pb2.TensorProto(
        dtype=dtypes_lib.variant.as_datatype_enum,
        tensor_shape=tensor_shape.TensorShape([]).as_proto(),
        variant_val=[
            tensor_pb2.VariantTensorDataProto(
                # Match registration in variant_op_registry.cc
                type_name=b"int",
                metadata=np.array(1, dtype=np.int32).tobytes())
        ])
    const_variant = constant_op.constant(variant_tensor)
    zeros_like = array_ops.zeros_like(const_variant)
    zeros_like_op = logging_ops.Print(
        zeros_like, [const_variant, zeros_like],
        message="Variant storing an int, input and output of zeros_like:").op

    # Smoke test -- ensure this executes without trouble.
    # Right now, non-numpy-compatible objects cannot be returned from a
    # session.run call; similarly, objects that can't be converted to
    # native numpy types cannot be passed to ops.convert_to_tensor.
    # TODO(ebrevdo): Add registration mechanism for
    # ops.convert_to_tensor and for session.run output.
    zeros_like_op.run()
