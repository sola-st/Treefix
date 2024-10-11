# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for use_resource in [False, True]:
    with self.subTest(use_resource=use_resource):
        a = variable_scope.get_variable(
            "var_{}".format(use_resource), [],
            initializer=init_ops.constant_initializer(10.0),
            use_resource=use_resource)
        guarantee_a = array_ops.guarantee_const(a)
        self.evaluate(a.initializer)
        self.assertEqual(10.0, self.evaluate(guarantee_a))
