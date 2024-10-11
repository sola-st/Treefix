# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py

def creator(next_creator, **kwargs):
    exit(next_creator(**kwargs))

# Save the state so we can clean up at the end.
graph = ops.get_default_graph()
old_creator_stack = graph._variable_creator_stack

try:
    scope = variable_scope.variable_creator_scope(creator)
    scope.__enter__()
    with variable_scope.variable_creator_scope(creator):
        with self.assertRaises(RuntimeError):
            scope.__exit__(None, None, None)
finally:
    graph._variable_creator_stack = old_creator_stack
