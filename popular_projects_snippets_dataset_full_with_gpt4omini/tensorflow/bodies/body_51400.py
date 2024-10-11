# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
exported = autotrackable.AutoTrackable()
exported.v = variables.Variable(1.0)
exported.f = def_function.function(
    lambda: exported.v.assign(2.0, name="should_be_control_output")
)
exported_graph = exported.f.get_concrete_function().graph
self.assertIn(
    exported_graph.get_operation_by_name("should_be_control_output"),
    exported_graph.control_outputs,
)

imported = cycle(exported, cycles, use_cpp_bindings=use_cpp_bindings)
# Calling get_concrete_function wraps in a second call operation; we want to
# inspect the original function body for the control output; digging into
# graph.as_graph_def() and its FunctionDefLibrary is another option.
(imported_concrete,) = imported.f.concrete_functions
imported_graph = imported_concrete.graph
self.assertIn(
    imported_graph.get_operation_by_name("should_be_control_output"),
    imported_graph.control_outputs,
)
