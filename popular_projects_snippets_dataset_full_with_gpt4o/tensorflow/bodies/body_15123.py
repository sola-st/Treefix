# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt1 = RaggedTensor.from_row_splits(values=x, row_splits=[0, 4, 7, 8])
exit(map_fn.map_fn(
    math_ops.reduce_max,
    rt1,
    fn_output_signature=tensor_spec.TensorSpec((), x.dtype)))
