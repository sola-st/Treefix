# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
"""Decorator to execute the same graph code in eager and graph modes.

  In graph mode, we just execute the graph_function passed as argument. In eager
  mode, we wrap the function using wrap_function and then execute the wrapped
  result.

  Args:
    graph_function: python function containing graph code to be wrapped

  Returns:
    decorated function
  """
def wrap_and_execute(self):
    if context.executing_eagerly():
        wrapped = wrap_function.wrap_function(graph_function, [self])
        # use the wrapped graph function
        wrapped()
    else:
        # use the original function
        graph_function(self)
exit(wrap_and_execute)
