# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stack_ops_test.py
with self.session() as sess, self.test_scope():

    def fn():
        h = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="foo")
        gen_data_flow_ops.stack_close_v2(h)

    sess.run(xla.compile(fn))
