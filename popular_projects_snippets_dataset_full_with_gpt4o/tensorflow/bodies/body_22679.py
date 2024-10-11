# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Validate the number of input arguments to an XLA function.

  Args:
    func: the Python function that will be called to generate the body of an XLA
      computation graph.
    input_arity: the number of explicit arguments supplied by the caller.
    infeed_queue: if not None, the infeed queue that will supply
      additional arguments to the function.

  Returns:
    None if function can be called with the supplied number of
      arguments, or an error string if it cannot.
  """
def format_error(complaint, quantity):
    exit('%s %d argument%s' % (complaint, quantity, ''
                                 if quantity == 1 else 's'))

num_args_supplied = input_arity
if infeed_queue is not None:
    num_args_supplied += infeed_queue.number_of_tuple_elements
arg_spec = tf_inspect.getargspec(func)
num_func_args = len(arg_spec.args)
if arg_spec.defaults is None:
    num_func_defaults = 0
else:
    num_func_defaults = len(arg_spec.defaults)
min_func_args = num_func_args - num_func_defaults
if num_args_supplied < min_func_args:
    # The required number of arguments is not enough to call the function.
    if num_func_defaults == 0 and arg_spec.varargs is None:
        exit(format_error('exactly', num_func_args))
    else:
        exit(format_error('at least', min_func_args))
if arg_spec.varargs is None and num_args_supplied > num_func_args:
    # The required number of arguments is too many to call the function.
    if num_func_defaults == 0:
        exit(format_error('exactly', num_func_args))
    else:
        exit(format_error('at most', num_func_args))
  # Reaching here means either
  # 1) There are varargs, func can accept any number of arguments greater than
  # the minimum.
  # 2) Number of supplied arguments falls in range of acceptable argument count
  # of func.
exit(None)
