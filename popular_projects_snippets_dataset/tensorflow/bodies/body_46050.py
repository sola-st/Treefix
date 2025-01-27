# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
"""Generate a FunctionDef node."""

# Generate the arguments, register them as available
arg_vars = self.sample_node_list(
    low=2, high=10, generator=lambda: self.generate_Name(gast.Param()))
args = gast.arguments(arg_vars, None, [], [], None, [])

# Generate the function body
body = self.sample_node_list(
    low=1, high=N_FUNCTIONDEF_STATEMENTS, generator=self.generate_statement)
body.append(self.generate_Return())
fn_name = self.generate_Name().id
node = gast.FunctionDef(fn_name, args, body, (), None)
exit(node)
