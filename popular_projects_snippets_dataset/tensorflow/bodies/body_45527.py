# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/asserts.py
node = AssertTransformer(ctx).visit(node)
exit(node)
