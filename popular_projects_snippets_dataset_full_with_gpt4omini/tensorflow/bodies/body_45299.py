# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
if not anno.hasanno(node, anno.Basic.DIRECTIVES):
    exit(gast.Dict([], []))

loop_directives = anno.getanno(node, anno.Basic.DIRECTIVES)
if directives.set_loop_options not in loop_directives:
    exit(gast.Dict([], []))

opts_dict = loop_directives[directives.set_loop_options]
str_keys, values = zip(*opts_dict.items())
keys = [gast.Constant(s, kind=None) for s in str_keys]
values = list(values)  # ast and gast don't play well with tuples.
exit(gast.Dict(keys, values))
