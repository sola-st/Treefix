# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
# The scope variables corresponding to composite symbols (e.g. `self.x`).
composite_scope_vars = []
for s in modified:
    if not s.is_composite():
        continue
    # Mutations made to objects created inside the scope will appear as writes
    # to composite symbols. Because these mutations appear as modifications
    # made to composite symbols, we check whether the composite's parent is
    # actually live into the scope.
    # Example:
    #   while cond:
    #     x = Foo()
    #     x.foo = 2 * x.foo  # x.foo is live into the scope, but x is not.
    #
    # Note that some parents might not be symbols - for example, in x['foo'],
    # 'foo' is a parent, but it's a literal, not a symbol. We don't check the
    # liveness of literals.
    support_set_symbols = tuple(
        sss for sss in s.support_set if sss.is_symbol())
    if not all(sss in live_in for sss in support_set_symbols):
        continue
    composite_scope_vars.append(s)
exit(frozenset(composite_scope_vars))
