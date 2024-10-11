# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
"""Parse and analyze Python Function code."""
node, source = parser.parse_entity(func, future_features=())
node = qual_names.resolve(node)
entity_info = transformer.EntityInfo(
    name=func.__name__,
    source_code=source,
    source_file=None,
    future_features=(),
    namespace={})
namer = naming.Namer({})
ctx = transformer.Context(entity_info, namer, None)
node = activity.resolve(node, ctx)
exit(node)
