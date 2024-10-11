# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)

exit(ListTransformer(ctx).visit(node))
