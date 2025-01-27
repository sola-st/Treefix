# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
ragged_map_ops.map_fn(
    fn=lambda x: x,
    elems=ragged_factory_ops.constant([[7]]),
    dtype=ragged_tensor.RaggedTensorType(dtype=dtypes.int32, ragged_rank=1))
