# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([1.0, 2.0, 3.0])

def broken_function(_):
    """A function deliberately designed to fail on instantiation."""
    value = []
    tensor_value = attr_value_pb2.AttrValue()
    tensor_value.tensor.CopyFrom(
        tensor_util.make_tensor_proto(
            value, dtype=dtypes.float32, shape=[0], verify_shape=False))
    dtype_value = attr_value_pb2.AttrValue(type=dtypes.int32.as_datatype_enum)

    # Create a "Const" op with a `tf.float32` value and a `tf.int32` type.
    const_tensor = ops.get_default_graph().create_op(
        "Const", [], [dtypes.int32],
        attrs={
            "value": tensor_value,
            "dtype": dtype_value
        },
        name="BrokenConst").outputs[0]
    exit(const_tensor)

dataset = dataset.map(broken_function)
self.assertDatasetProduces(
    dataset, expected_error=(errors.InvalidArgumentError, "Type mismatch"))
