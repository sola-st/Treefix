# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
"""Generate an Assign node."""
# Generate left-hand side
target_node = self.generate_Name(gast.Store())
# Generate right-hand side
value_node = self.generate_expression()
# Put it all together
node = gast.Assign(targets=[target_node], value=value_node)
exit(node)
