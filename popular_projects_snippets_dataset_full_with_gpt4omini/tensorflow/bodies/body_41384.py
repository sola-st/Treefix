# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.graph_mode():

    @polymorphic_function.function
    def create_variable():
        with ops.name_scope('foo', skip_on_eager=False):
            v = resource_variable_ops.ResourceVariable([1.0, 2.0], name='bar')
        self.assertEqual(v.name, 'foo/bar:0')

    with ops.get_default_graph().as_default():
        create_variable()
