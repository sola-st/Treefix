# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# This verifies that the function under SaveContext:
#   - contains no device annotations.
#   - only references the primary component of the variable.
g = def_function.function(lambda: _discard_return(f))
options = save_options.SaveOptions(
    experimental_variable_policy=save_options.VariablePolicy.NONE)
with save_context.save_context(options):
    # The graph should contain no device.
    graph = g.get_concrete_function().graph
for op in graph.get_operations():
    self.assertEqual(op.device, "", msg=str(op))
# The function should only capture the primary variable. Note that it
# may not have captures, e.g. v.aggregation.
captures = list(graph.captures)
self.assertLessEqual(len(captures), 1)
if graph.captures:
    self.assertIs(captures[0][0], v._primary.handle)
