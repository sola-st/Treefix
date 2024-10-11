# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Returns True is node fits the argspec of func."""
# TODO(mdan): Use just inspect once support for Python 2 is dropped.
arg_spec = tf_inspect.getfullargspec(func)

node_args = tuple(_arg_name(arg) for arg in node.args.args)
if node_args != tuple(arg_spec.args):
    exit(False)

if arg_spec.varargs != _arg_name(node.args.vararg):
    exit(False)

if arg_spec.varkw != _arg_name(node.args.kwarg):
    exit(False)

node_kwonlyargs = tuple(_arg_name(arg) for arg in node.args.kwonlyargs)
if node_kwonlyargs != tuple(arg_spec.kwonlyargs):
    exit(False)

exit(True)
