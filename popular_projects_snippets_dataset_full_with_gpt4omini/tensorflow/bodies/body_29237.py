# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    (tensor_spec.TensorSpec([32], dtypes.float32),
     tensor_spec.TensorSpec([], dtypes.float32)),
    (tensor_spec.TensorSpec([None], dtypes.float32),
     tensor_spec.TensorSpec([], dtypes.float32)),
    (sparse_tensor.SparseTensorSpec([32, None], dtypes.float32),
     sparse_tensor.SparseTensorSpec([None], dtypes.float32)),
    (sparse_tensor.SparseTensorSpec([None, 4], dtypes.float32),
     sparse_tensor.SparseTensorSpec([4], dtypes.float32)),
    (ragged_tensor.RaggedTensorSpec([32, None, None], dtypes.float32, 2),
     ragged_tensor.RaggedTensorSpec([None, None], dtypes.float32, 1)),
    (ragged_tensor.RaggedTensorSpec([None, None, None], dtypes.float32, 2),
     ragged_tensor.RaggedTensorSpec([None, None], dtypes.float32, 1)),
    ({
        "a":
            tensor_spec.TensorSpec([128], dtypes.float32),
        "b": (sparse_tensor.SparseTensorSpec([128, 2, 2], dtypes.int32),
              tensor_spec.TensorSpec([None], dtypes.string))
    }, {
        "a":
            tensor_spec.TensorSpec([], dtypes.float32),
        "b": (sparse_tensor.SparseTensorSpec([2, 2], dtypes.int32),
              tensor_spec.TensorSpec([], dtypes.string))
    }),
]

def reduce_fn(x, y):
    element_structure, expected_unbatched_structure = y
    exit(x + combinations.combine(
        element_structure=element_structure,
        expected_unbatched_structure=expected_unbatched_structure))

exit(functools.reduce(reduce_fn, cases, []))
