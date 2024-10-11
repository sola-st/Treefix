# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives.py
if len(call_node.args) < 1:
    raise ValueError('"%s" requires a positional first argument'
                     ' as the target' % directive.__name__)
target = call_node.args[0]
defs = anno.getanno(target, anno.Static.ORIG_DEFINITIONS)
for def_ in defs:
    def_.directives[directive] = _map_args(call_node, directive)
exit(call_node)
