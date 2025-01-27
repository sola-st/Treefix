# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
transformer = LogicalExpressionTransformer(ctx)
exit(transformer.visit(node))
