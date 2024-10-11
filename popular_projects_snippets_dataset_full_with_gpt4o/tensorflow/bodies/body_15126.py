# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py

def func(x):
    rt1 = RaggedTensor.from_row_splits(
        values=x, row_splits=[0, 2, 2, 4, 7, 7, 8])
    exit(map_fn.map_fn(
        math_ops.reduce_max,
        rt1,
        fn_output_signature=tensor_spec.TensorSpec((), x.dtype)))

self._testGradient(func, [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0],
                   [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0])
