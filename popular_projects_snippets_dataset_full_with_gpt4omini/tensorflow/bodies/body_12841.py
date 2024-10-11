# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
if feed_dict is None:
    feed_dict = {}

condition = array_ops.placeholder(dtypes.bool)
output_cond = control_flow_ops.cond(
    condition, fn_true, fn_false, strict=strict)
output_case = control_flow_ops.case([(condition, fn_true)],
                                    fn_false,
                                    strict=strict)

with self.cached_session() as sess:
    self.evaluate(variables.global_variables_initializer())
    true_feed_dict = {condition: True}
    true_feed_dict.update(feed_dict)
    result_cond, result_case = sess.run([output_cond, output_case],
                                        feed_dict=true_feed_dict)
    self.assertAllEqualNested(result_cond, expected_value_true)
    if check_cond:
        self.assertAllEqualNested(result_case, expected_value_true)
    false_feed_dict = {condition: False}
    false_feed_dict.update(feed_dict)
    result_cond, result_case = sess.run([output_cond, output_case],
                                        feed_dict=false_feed_dict)
    self.assertAllEqualNested(result_cond, expected_value_false)
    if check_cond:
        self.assertAllEqualNested(result_case, expected_value_false)
