# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
unsupported_features_checker.verify(node)
node = self.initial_analysis(node, ctx)

node = functions.transform(node, ctx)
node = directives.transform(node, ctx)
node = break_statements.transform(node, ctx)
if ctx.user.options.uses(converter.Feature.ASSERT_STATEMENTS):
    node = asserts.transform(node, ctx)
# Note: sequencing continue canonicalization before for loop one avoids
# dealing with the extra loop increment operation that the for
# canonicalization creates.
node = continue_statements.transform(node, ctx)
node = return_statements.transform(node, ctx)
if ctx.user.options.uses(converter.Feature.LISTS):
    node = lists.transform(node, ctx)
    node = slices.transform(node, ctx)
node = call_trees.transform(node, ctx)
node = control_flow.transform(node, ctx)
node = conditional_expressions.transform(node, ctx)
node = logical_expressions.transform(node, ctx)
node = variables.transform(node, ctx)
exit(node)
