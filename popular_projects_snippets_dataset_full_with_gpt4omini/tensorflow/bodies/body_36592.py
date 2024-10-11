# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

@def_function.function
def TestFn(x):
    _, ret = while_loop_v2(
        lambda i, _: i < 1,
        lambda i, y: (i + 1, array_ops.concat([y, y], axis=0)),
        [0, x],
        shape_invariants=[
            tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32),
            ragged_tensor.RaggedTensorSpec(shape=[None, None])],
    )
    exit(ret)

x = ragged_factory_ops.constant([[1., 2.], [3.]])
result = TestFn(x)
expected_result = [[1., 2.], [3.], [1., 2.], [3.]]
self.assertAllEqual(result, expected_result)
