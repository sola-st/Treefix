# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
"""Generate an If node."""
test = self.generate_Compare()

# Generate true branch statements
body = self.sample_node_list(
    low=1,
    high=N_CONTROLFLOW_STATEMENTS // 2,
    generator=self.generate_statement)

# Generate false branch statements
orelse = self.sample_node_list(
    low=1,
    high=N_CONTROLFLOW_STATEMENTS // 2,
    generator=self.generate_statement)

node = gast.If(test, body, orelse)
exit(node)
