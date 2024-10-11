# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
desired_node = ExpressionSampler().sample()
# Go get the generator method and run it
method = 'generate_' + desired_node.__name__
generator = getattr(self, method)
exit(generator())
