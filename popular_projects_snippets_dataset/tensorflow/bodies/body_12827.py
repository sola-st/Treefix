# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with ops.Graph().as_default():
    writer = summary_ops_v2.create_file_writer(self.get_temp_dir())
    with writer.as_default(), summary_ops_v2.always_record_summaries():
        op = control_flow_ops.cond(
            constant_op.constant(1) >= 0,
            lambda: control_flow_ops.group(summary_ops_v2.scalar("loss", 0.2)),
            control_flow_ops.no_op)
        self.evaluate(variables.global_variables_initializer())
        self.evaluate(summary_ops_v2.summary_writer_initializer_op())
        self.assertEqual(self.evaluate(op), True)
