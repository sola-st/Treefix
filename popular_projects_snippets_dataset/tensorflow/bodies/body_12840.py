# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
condition = array_ops.placeholder(dtypes.bool)
output_cond = control_flow_ops.cond(
    condition, fn_true, fn_false, strict=strict)
self.assertEqual(
    _raw_nested_shape(_get_nested_shape(output_cond)),
    _raw_nested_shape(expected_shape))

output_case = control_flow_ops.case([(condition, fn_true)],
                                    fn_false,
                                    strict=strict)
self.assertEqual(
    _raw_nested_shape(_get_nested_shape(output_case)),
    _raw_nested_shape(expected_shape))
