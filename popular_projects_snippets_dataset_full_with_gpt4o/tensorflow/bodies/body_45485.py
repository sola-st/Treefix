# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
node = self.generic_visit(node)

# TODO(mdan): This is insufficient if target is a function argument.
# In the case of function arguments, we need to add the list to the
# function's return value, because it is being modified.
# TODO(mdan): Checking just the name is brittle, can it be improved?
if isinstance(node.func, gast.Attribute):
    func_name = node.func.attr
    if func_name == 'append' and (len(node.args) == 1):
        node = self._replace_append_call(node)
    elif func_name == 'pop' and (len(node.args) <= 1):
        node = self._replace_pop_call(node)
    elif (func_name == 'stack' and (len(node.args) == 1) and
          (not node.keywords or node.keywords[0].arg == 'strict')):
        # This avoids false positives with keyword args.
        # TODO(mdan): handle kwargs properly.
        node = self._replace_stack_call(node)

exit(node)
