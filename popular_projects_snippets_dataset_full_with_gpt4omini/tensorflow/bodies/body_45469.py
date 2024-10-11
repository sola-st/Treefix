# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements.py
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)

transformer = BreakTransformer(ctx)
node = transformer.visit(node)
exit(node)
