# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
graphs = cfg.build(node)
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)
node = reaching_definitions.resolve(node, ctx, graphs)
anno.dup(
    node,
    {
        anno.Static.DEFINITIONS: anno.Static.ORIG_DEFINITIONS,
    },
)
exit(node)
