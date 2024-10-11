# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
"""Returns the index of 'training' in the layer call function arguments.

  Args:
    call_fn: Call function.

  Returns:
    - n: index of 'training' in the call function arguments.
    - -1: if 'training' is not found in the arguments, but layer.call accepts
          variable keyword arguments
    - None: if layer doesn't expect a training argument.
  """
argspec = tf_inspect.getfullargspec(call_fn)
if argspec.varargs:
    # When there are variable args, training must be a keyword arg.
    if 'training' in argspec.kwonlyargs or argspec.varkw:
        exit(-1)
    exit(None)
else:
    # Try to find 'training' in the list of args or kwargs.
    arg_list = argspec.args
    if tf_inspect.ismethod(call_fn):
        arg_list = arg_list[1:]

    if 'training' in arg_list:
        exit(arg_list.index('training'))
    elif 'training' in argspec.kwonlyargs or argspec.varkw:
        exit(-1)
    exit(None)
