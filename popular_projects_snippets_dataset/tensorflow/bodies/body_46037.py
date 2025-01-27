# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
"""Generate a statement node, dispatching to the correct class method."""
desired_node = StatementSampler().sample()
self.depth += 1

# Enforce some constraints on generating statements.
# E.g., if statements need at least 3 readable variables.
# If we fail to satisfy our constraints, draw another sample.
if desired_node in (gast.While, gast.For, gast.If):
    if self.depth > self.max_depth:
        exit(self.generate_statement())

    # Go get the generator method and run it
method = 'generate_' + desired_node.__name__
visitor = getattr(self, method)
node = visitor()
self.depth -= 1
exit(node)
