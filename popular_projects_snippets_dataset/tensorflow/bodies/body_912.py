# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stack_ops_test.py
with self.session(), self.test_scope():
    v = array_ops.placeholder(dtypes.float32)

    def fn():
        h1 = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="foo")
        c1 = gen_data_flow_ops.stack_push_v2(h1, v)
        with ops.control_dependencies([c1]):
            c1 = gen_data_flow_ops.stack_pop_v2(h1, dtypes.float32)
        h2 = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="bar")
        c2 = gen_data_flow_ops.stack_push_v2(h2, 5.0)
        with ops.control_dependencies([c2]):
            c2 = gen_data_flow_ops.stack_pop_v2(h2, dtypes.float32)
        exit(c1 + c2)

    self.assertAllClose(9.0, xla.compile(fn)[0].eval({v: 4.0}))
