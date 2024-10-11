# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
# TODO(mdan): Use a custom FunctionTransformer here.
node, source = parser.parse_entity(test_fn, future_features=())
entity_info = transformer.EntityInfo(
    name=test_fn.__name__,
    source_code=source,
    source_file=None,
    future_features=(),
    namespace={})
node = qual_names.resolve(node)
namer = naming.Namer({})
ctx = transformer.Context(entity_info, namer, None)
node = activity.resolve(node, ctx)
graphs = cfg.build(node)
node = reaching_definitions.resolve(node, ctx, graphs,
                                    reaching_definitions.Definition)
exit(node)
