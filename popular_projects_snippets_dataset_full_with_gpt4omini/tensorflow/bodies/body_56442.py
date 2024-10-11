# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
# Produce GraphDef containing a ops producing and consuming resources.
graph = ops.Graph()
with graph.as_default():
    var = resource_variable_ops.ResourceVariable(1.0)
    var_assign = var.assign(2.0)
    # Use an op that requires handle shape to be set.
    var_shape = resource_variable_ops.variable_shape(var.handle)
    init = variables.global_variables_initializer()
graph_def = graph.as_graph_def()

# Import the GraphDef.
with ops.Graph().as_default():
    # pylint: disable=unused-variable
    imported_var, imported_assign, imported_shape, imported_init = (
        importer.import_graph_def(
            graph_def,
            return_elements=[var.name, var_assign.name, var_shape.name,
                             init.name]))

    # Make sure the handle shape is set on the imported variable.
    new_var_shape = resource_variable_ops.variable_shape(imported_var)
    # pylint: enable=unused-variable

    # Run the imported graph.
    # TODO(b/76173421): make this work (currently DCHECKS)
    # with self.cached_session() as sess:
    #   self.evaluate(imported_init)
    #   self.assertEqual(self.evaluate(imported_var), 1.0)
    #   self.assertEqual(self.evaluate(imported_assign), 2.0)
    #   self.assertEqual(list(self.evaluate(imported_shape)), [])
    #   self.assertEqual(list(self.evaluate(new_var_shape)), [])
