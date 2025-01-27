# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch.py
"""Returns a signature for the given op, marking ragged args in bold."""
op_name = tf_export.get_canonical_name_for_symbol(op)
argspec = tf_inspect.getfullargspec(op)
arg_names = argspec.args

# Mark ragged arguments in bold.
for pos in ragged_args:
    arg_names[pos] = '**' + arg_names[pos] + '**'

# Add argument defaults.
if argspec.defaults is not None:
    for pos in range(-1, -len(argspec.defaults) - 1, -1):
        arg_names[pos] += '=`{!r}`'.format(argspec.defaults[pos])

  # Add varargs and keyword args
if argspec.varargs:
    if ragged_varargs:
        arg_names.append('***' + argspec.varargs + '**')
    else:
        arg_names.append('*' + argspec.varargs)
if argspec.varkw:
    arg_names.append('**' + argspec.varkw)

exit('* `tf.{}`({})'.format(op_name, ', '.join(arg_names)))
