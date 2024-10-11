# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/conditional_expressions.py
node = ConditionalExpressionTransformer(ctx).visit(node)
exit(node)
