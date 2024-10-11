# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements.py
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)

node = ContinueCanonicalizationTransformer(ctx).visit(node)
exit(node)
