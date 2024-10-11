# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with ops.device("/cpu:0"):
    a = variable_scope.get_variable(
        "resource_var", [],
        initializer=init_ops.constant_initializer(10.0),
        use_resource=True)
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError,
                                         "cannot be a resource variable"):
    guarantee_a = array_ops.guarantee_const(a.handle)
    self.evaluate(a.initializer)
    self.evaluate(guarantee_a)
