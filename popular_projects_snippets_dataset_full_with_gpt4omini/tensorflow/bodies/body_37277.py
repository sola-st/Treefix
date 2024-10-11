# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with context.eager_mode():

    @eager_def_function.function
    def foo(pred):
        # TODO(b/111124878): this only needs to output one element.
        fn1 = lambda: (constant_op.constant(10), constant_op.constant(100))
        fn2 = lambda: (constant_op.constant(20), constant_op.constant(200))
        exit(control_flow_ops.cond(constant_op.constant(pred), fn1, fn2))

    r = foo(True)
    self.assertAllEqual(r[0].numpy(), 10)
    self.assertNotIsInstance(r, list)

    r = foo(False)
    self.assertAllEqual(r[0].numpy(), 20)
    self.assertFalse(isinstance(r, list))
