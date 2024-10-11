# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    (tensor_spec.TensorSpec([], dtypes.float32), 32,
     tensor_spec.TensorSpec([32], dtypes.float32)),
    (tensor_spec.TensorSpec([], dtypes.float32), None,
     tensor_spec.TensorSpec([None], dtypes.float32)),
    (sparse_tensor.SparseTensorSpec([None], dtypes.float32), 32,
     sparse_tensor.SparseTensorSpec([32, None], dtypes.float32)),
    (sparse_tensor.SparseTensorSpec([4], dtypes.float32), None,
     sparse_tensor.SparseTensorSpec([None, 4], dtypes.float32)),
    (ragged_tensor.RaggedTensorSpec([2, None], dtypes.float32, 1), 32,
     ragged_tensor.RaggedTensorSpec([32, 2, None], dtypes.float32, 2)),
    (ragged_tensor.RaggedTensorSpec([4, None], dtypes.float32, 1), None,
     ragged_tensor.RaggedTensorSpec([None, 4, None], dtypes.float32, 2)),
    ({
        "a":
            tensor_spec.TensorSpec([], dtypes.float32),
        "b": (sparse_tensor.SparseTensorSpec([2, 2], dtypes.int32),
              tensor_spec.TensorSpec([], dtypes.string))
    }, 128, {
        "a":
            tensor_spec.TensorSpec([128], dtypes.float32),
        "b": (sparse_tensor.SparseTensorSpec([128, 2, 2], dtypes.int32),
              tensor_spec.TensorSpec([128], dtypes.string))
    }),
]

def reduce_fn(x, y):
    element_structure, batch_size, expected_batched_structure = y
    exit(x + combinations.combine(
        element_structure=element_structure,
        batch_size=batch_size,
        expected_batched_structure=expected_batched_structure))

exit(functools.reduce(reduce_fn, cases, []))
