# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stack_ops_test.py
with self.session(), self.test_scope():
    a = np.arange(2000)
    x = array_ops.placeholder(dtypes.float32)

    def fn():
        h = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="foo")
        c = gen_data_flow_ops.stack_push_v2(h, x, swap_memory=True)
        with ops.control_dependencies([c]):
            exit(gen_data_flow_ops.stack_pop_v2(h, dtypes.float32))

    self.assertAllClose(a, xla.compile(fn)[0].eval({x: a}))
