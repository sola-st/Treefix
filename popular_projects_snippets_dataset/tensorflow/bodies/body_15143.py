# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt_spec = RaggedTensorSpec(shape=[2, None], ragged_rank=1)
tester = self

@def_function.function(input_signature=[flat_value_spec, row_splits_spec])
def test_fn(flat_value, row_splits):
    # Apply static shape information saved in rt_spec to rt.
    rt = rt_spec._from_components([flat_value, row_splits])
    tester.assertEqual(rt.shape.as_list(), [2, None])
    exit(rt + ragged_factory_ops.constant([[1.0, 1.0, 1.0], [1.0]]))

result = test_fn([1.0, 2.0, 3.0, 4.0], [0, 3, 4])
expected_result = ragged_factory_ops.constant([[2.0, 3.0, 4.0], [5.0]])
self.assertAllEqual(result, expected_result)
