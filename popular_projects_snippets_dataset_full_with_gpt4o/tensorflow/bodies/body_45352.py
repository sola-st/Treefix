# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables.py
# Only the loads which existed in the original code are overloaded.
if not anno.hasanno(node, anno.Static.ORIG_DEFINITIONS):
    exit(node)
if isinstance(node.ctx, gast.Load):
    node = templates.replace_as_expression('ag__.ld(var_)', var_=node)
exit(node)
