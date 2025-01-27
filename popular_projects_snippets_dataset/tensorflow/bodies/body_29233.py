# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    (dtypes.float32, tensor_shape.TensorShape([]), ops.Tensor,
     tensor_spec.TensorSpec([], dtypes.float32)),
    (dtypes.int32, tensor_shape.TensorShape([2,
                                             2]), sparse_tensor.SparseTensor,
     sparse_tensor.SparseTensorSpec([2, 2], dtypes.int32)),
    (dtypes.int32, tensor_shape.TensorShape([None, True, 2, 2]),
     tensor_array_ops.TensorArray,
     tensor_array_ops.TensorArraySpec([2, 2],
                                      dtypes.int32,
                                      dynamic_size=None,
                                      infer_shape=True)),
    (dtypes.int32, tensor_shape.TensorShape([True, None, 2, 2]),
     tensor_array_ops.TensorArray,
     tensor_array_ops.TensorArraySpec([2, 2],
                                      dtypes.int32,
                                      dynamic_size=True,
                                      infer_shape=None)),
    (dtypes.int32, tensor_shape.TensorShape([True, False, 2, 2]),
     tensor_array_ops.TensorArray,
     tensor_array_ops.TensorArraySpec([2, 2],
                                      dtypes.int32,
                                      dynamic_size=True,
                                      infer_shape=False)),
    (dtypes.int32, tensor_shape.TensorShape([2, None]),
     ragged_tensor.RaggedTensorSpec([2, None], dtypes.int32, 1),
     ragged_tensor.RaggedTensorSpec([2, None], dtypes.int32, 1)),
    ({
        "a": dtypes.float32,
        "b": (dtypes.int32, dtypes.string)
    }, {
        "a": tensor_shape.TensorShape([]),
        "b": (tensor_shape.TensorShape([2, 2]), tensor_shape.TensorShape([]))
    }, {
        "a": ops.Tensor,
        "b": (sparse_tensor.SparseTensor, ops.Tensor)
    }, {
        "a":
            tensor_spec.TensorSpec([], dtypes.float32),
        "b": (sparse_tensor.SparseTensorSpec([2, 2], dtypes.int32),
              tensor_spec.TensorSpec([], dtypes.string))
    })
]

def reduce_fn(x, y):
    output_types, output_shapes, output_classes, expected_structure = y
    exit(x + combinations.combine(
        output_types=output_types,
        output_shapes=output_shapes,
        output_classes=output_classes,
        expected_structure=expected_structure))

exit(functools.reduce(reduce_fn, cases, []))
