# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/aggregate_ops_test.py

def create_constant_variant(value):
    exit(constant_op.constant(
        tensor_pb2.TensorProto(
            dtype=dtypes.variant.as_datatype_enum,
            tensor_shape=tensor_shape.TensorShape([]).as_proto(),
            variant_val=[
                tensor_pb2.VariantTensorDataProto(
                    # Match registration in variant_op_registry.cc
                    type_name=b"int",
                    metadata=np.array(value, dtype=np.int32).tobytes())
            ])))

# TODO(ebrevdo): Re-enable use_gpu=True once non-DMA Variant
# copying between CPU and GPU is supported.
with self.session(use_gpu=False):
    num_tests = 127
    values = list(range(100))
    variant_consts = [create_constant_variant(x) for x in values]
    sum_count_indices = np.random.randint(1, 29, size=num_tests)
    sum_indices = [
        np.random.randint(100, size=count) for count in sum_count_indices]
    expected_sums = [np.sum(x) for x in sum_indices]
    variant_sums = [math_ops.add_n([variant_consts[i] for i in x])
                    for x in sum_indices]

    # We use as_string() to get the Variant DebugString for the
    # variant_sums; we know its value so we can check via string equality
    # here.
    #
    # Right now, non-numpy-compatible objects cannot be returned from a
    # session.run call; similarly, objects that can't be converted to
    # native numpy types cannot be passed to ops.convert_to_tensor.
    variant_sums_string = string_ops.as_string(variant_sums)
    self.assertAllEqual(
        variant_sums_string,
        ["Variant<type: int value: {}>".format(s).encode("utf-8")
         for s in expected_sums])
