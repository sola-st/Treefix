# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions.py
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)

exit(FunctionTransformer(ctx).visit(node))
