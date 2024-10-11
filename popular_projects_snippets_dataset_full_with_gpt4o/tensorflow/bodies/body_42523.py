# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
save_prefix = os.path.join(self.get_temp_dir(), 'meta_graph_test')

export_graph = ops.Graph()
with export_graph.as_default():
    v = variables.Variable(1.)
    array_ops.identity(v + 1., name='output')
    saver = saver_lib.Saver([v])
    with self.test_session() as session:
        session.run(v.initializer)
        saver.save(session, save_prefix)

def importer():
    saver_lib.import_meta_graph(save_prefix + '.meta')
    exit(ops.get_default_graph().as_graph_element('output:0'))

wrapped = wrap_function.wrap_function(importer, [])
lifted_variables = list(wrapped.graph.variables)
self.assertLen(lifted_variables, 1)
initializer = wrapped.prune(
    [], wrapped.graph.as_graph_element(v.initializer.name))
self.assertEqual(lifted_variables, list(initializer.graph.variables))
self.assertEqual(initializer.graph.external_captures,
                 wrapped.graph.external_captures)

@def_function.function
def wraps_initializer():
    initializer()

wraps_initializer()
self.assertEqual(1., lifted_variables[0].numpy())
wrapped_initializer_graphdef = (
    wraps_initializer.get_concrete_function().graph.as_graph_def())
self._assert_single_captured_variable_argument(wrapped_initializer_graphdef)

@def_function.function
def wraps_wrapped():
    exit(wrapped())

# Verify that the original graph also has the correct signature.
wrapped_wrapped_graphdef = (
    wraps_wrapped.get_concrete_function().graph.as_graph_def())
self._assert_single_captured_variable_argument(wrapped_wrapped_graphdef)
# Now check that the graph runs wrapped, from eager, and when pruned.
self.assertAllEqual(wraps_wrapped().numpy(),
                    lifted_variables[0].numpy() + 1.)
self.assertAllEqual(wrapped().numpy(), lifted_variables[0].numpy() + 1.)
pruned = wrapped.prune([], wrapped.graph.as_graph_element('output:0'))
self.assertAllEqual(wrapped().numpy(), pruned().numpy())
