# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
"""Ensure a function has only a single return, at the end."""
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)

# Note: Technically, these two could be merged into a single walk, but
# keeping them separate helps with readability.
node = ConditionalReturnRewriter(ctx).visit(node)

node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)
transformer = ReturnStatementsTransformer(
    ctx, allow_missing_return=default_to_null_return)
node = transformer.visit(node)
exit(node)
