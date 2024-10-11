# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
# Expressions that use pop() are converted to a statement + expression.
#
# For example:
#
#   print(target.pop())
#
# ... is converted to:
#
#   target, target_pop = ag__.list_pop(target)
#   print(target_pop)
#
# Here, we just generate the variable name and swap it in,
# and _generate_pop_operation will handle the rest.
#
# Multiple uses of pop() are allowed:
#
#   print(tartget.pop(), target.pop())
#   print(tartget.pop().pop())
#
assert isinstance(node.func, gast.Attribute)
scope = anno.getanno(node, NodeAnno.ARGS_SCOPE)
target_node = node.func.value

# Attempt to use a related name if one exists. Otherwise use something
# generic.
if anno.hasanno(target_node, anno.Basic.QN):
    target_name = anno.getanno(target_node, anno.Basic.QN).ssf()
else:
    target_name = 'list_'
pop_var_name = self.ctx.namer.new_symbol(target_name, scope.referenced)

stmt = self.state[_Statement]
if stmt.pop_uses is None:
    stmt.pop_uses = []
stmt.pop_uses.append((node, pop_var_name))

exit(templates.replace_as_expression('var_name', var_name=pop_var_name))
