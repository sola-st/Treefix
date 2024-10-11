# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
_, ret = while_loop_v2(
    lambda i, _: i < 1,
    lambda i, y: (i + 1, array_ops.concat([y, y], axis=0)),
    [0, x],
    shape_invariants=[
        tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32),
        ragged_tensor.RaggedTensorSpec(shape=[None, None])],
)
exit(ret)
