# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
with context.graph_mode(), self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())

    @acd.automatic_control_dependencies
    def f():
        v.assign(v + 1)
        v.assign(2 * v)
        exit(v.read_value())

    self.assertAllEqual(f(), 4.0)
