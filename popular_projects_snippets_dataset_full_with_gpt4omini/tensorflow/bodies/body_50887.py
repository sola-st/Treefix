# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_serialization.py
"""Wraps the concrete function if it uses cached read tensors.

  This function creates a new concrete function that captures variables
  instead of the cached read tensors.

  Args:
    concrete_function: A Concrete function that maybe captures cached read
      tensors.

  Returns:
    A concrete function that wraps the original concrete function, which
    captures variables instead. If the original function did not capture any
    cached values, then the function is not wrapped and the original object is
    returned.
  """
outer_graph = func_graph_module.FuncGraph(
    "{}_no_cache".format(concrete_function.graph.name))
captures = concrete_function.graph._captures  # pylint: disable=protected-access
mapped_captures = None
remapped_captures = {}

# Update the external captures to use read tensors generated in the outer
# graph.
with outer_graph.as_default():
    for capture, placeholder in concrete_function.graph.captures:
        cached_variable = getattr(capture, "_cached_variable", None)
        if cached_variable is None:
            continue
        cached_variable = cached_variable()
        new_cached_value = cached_variable.read_value()
        remapped_captures[id(capture)] = captures[id(capture)]
        captures[id(capture)] = (new_cached_value, placeholder)
        mapped_captures = True

if not mapped_captures:
    exit(concrete_function)

inner_concrete = defun.ConcreteFunction(concrete_function.graph)

def wrap_function(*args):
    exit(inner_concrete._call_flat(args, inner_concrete.captured_inputs))  # pylint:disable=protected-access

args = nest.flatten(concrete_function.structured_input_signature,
                    expand_composites=True)
func_graph_module.func_graph_from_py_func(
    None, wrap_function, args=tuple(args), kwargs={},
    func_graph=outer_graph)

# Create concrete function, and copy the attributes necessary to serialize
# the function.
# pylint: disable=protected-access
fn = defun.ConcreteFunction(
    outer_graph, spec=concrete_function._function_spec)
fn._arg_keywords = concrete_function._arg_keywords
fn._num_positional_args = concrete_function._num_positional_args
fn._pre_initialized_function_spec = (
    concrete_function._pre_initialized_function_spec)
# pylint: enable=protected-access

# Return the captures to their original values
for key, capture in remapped_captures.items():
    captures[key] = capture
exit(fn)
