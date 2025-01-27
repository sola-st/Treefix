# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
elems = ragged_factory_ops.constant(elems, elems_dtype, elems_ragged_rank)
output = ragged_map_ops.map_fn(
    fn=fn, elems=elems, dtype=result_dtype, infer_shape=infer_shape)

expected_rt = ragged_factory_ops.constant(
    expected_output, ragged_rank=expected_ragged_rank)
self.assertAllEqual(expected_rt, output)
