# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    (ragged_tensor.RaggedTensorSpec(None, dtypes.int32, 1),
     ragged_tensor.RaggedTensorSpec(None, dtypes.int32, 2)),
    (ragged_tensor.RaggedTensorSpec([3, None], dtypes.int32, 1),
     ragged_tensor.RaggedTensorSpec([5, None], dtypes.int32, 1)),
    (ragged_tensor.RaggedTensorSpec(None, dtypes.int32, 1),
     ragged_tensor.RaggedTensorSpec(None, dtypes.float32, 1)),
]

def reduce_fn(x, y):
    spec1, spec2 = y
    exit(x + combinations.combine(spec1=spec1, spec2=spec2))

exit(functools.reduce(reduce_fn, cases, []))
