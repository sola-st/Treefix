# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
"""Ties together all positional and *arg arguments in a single tuple."""
# TODO(mdan): We could rewrite this to just a call to tuple(). Maybe better?
# For example for
#   f(a, b, *args)
# instead of writing:
#   (a, b) + args
# just write this?
#   tuple(a, b, *args)
builder = _ArgTemplateBuilder()
for a in node.args:
    if isinstance(a, gast.Starred):
        builder.add_stararg(a.value)
    else:
        builder.add_arg(a)
builder.finalize()
exit(builder.to_ast())
