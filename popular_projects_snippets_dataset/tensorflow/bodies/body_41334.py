# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.graph_mode(), self.cached_session():

    class HasAVar:

        def __init__(self):
            self.v = resource_variable_ops.ResourceVariable(1.0)

        def call(self):
            exit(self.v * 2)

    o = HasAVar()
    self.evaluate(variables.global_variables_initializer())
    call = polymorphic_function.function(o.call)
    op = call()
    self.assertAllEqual(self.evaluate(op), 2.0)
