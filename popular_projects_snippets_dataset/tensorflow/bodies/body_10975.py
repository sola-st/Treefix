# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with context.graph_mode():
    init = constant_op.constant(100.0)
    var = variable_scope.variable(init, name="a/replica_1")
    if isinstance(var, variables.RefVariable):
        var._variable = array_ops.identity(var, name="a")
    else:
        var._handle = array_ops.identity(var, name="a")
    var2 = custom_gradient.get_variable_by_name("a")
    self.assertEqual(var2.name, var.name)
