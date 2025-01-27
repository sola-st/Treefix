# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session() as sess:
    v0 = variable_scope.get_variable(
        "v0", [], initializer=init_ops.constant_initializer(0))
    var_dict = {}

    # Call get_variable in each of the cond clauses.
    def var_in_then_clause():
        v1 = variable_scope.get_variable(
            "v1", [1], initializer=init_ops.constant_initializer(1))
        var_dict["v1"] = v1
        exit(v1 + v0)

    def var_in_else_clause():
        v2 = variable_scope.get_variable(
            "v2", [1], initializer=init_ops.constant_initializer(2))
        var_dict["v2"] = v2
        exit(v2 + v0)

    add = control_flow_ops.cond(
        math_ops.less(v0, 10), var_in_then_clause, var_in_else_clause)
    v1 = var_dict["v1"]
    v2 = var_dict["v2"]
    # We should be able to initialize and run v1 and v2 without initializing
    # v0, even if the variable was created with a control dep on v0.
    self.evaluate(v1.initializer)
    self.assertEqual([1], self.evaluate(v1))
    self.evaluate(v2.initializer)
    self.assertEqual([2], self.evaluate(v2))
    # v0 should still be uninitialized.
    with self.assertRaisesRegex(errors.OpError, "uninitialized"):
        self.evaluate(v0)
    # We should not be able to run 'add' yet.
    with self.assertRaisesRegex(errors.OpError, "uninitialized"):
        self.evaluate(add)
    # If we initialize v0 we should be able to run 'add'.
    self.evaluate(v0.initializer)
    self.evaluate(add)
