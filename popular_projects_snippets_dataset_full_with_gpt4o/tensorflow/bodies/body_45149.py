# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
# The loop variables corresponding to composite symbols (e.g. `self.x`).
composite_loop_vars = []
for s in modified_symbols:
    if not s.is_composite():
        continue
    # Mutations made to objects created inside the loop will appear as writes
    # to composite symbols. Because these mutations appear as modifications
    # made to composite symbols, we check whether the composite's parent is
    # actually live into the loop.
    # Example:
    #   while cond:
    #     x = Foo()
    #     x.foo = 2 * x.foo  # x.foo is live into the loop, but x is not.
    #
    # Note that some parents might not be symbols - for example, in x['foo'],
    # 'foo' is a parent, but it's a literal, not a symbol. We don't check the
    # liveness of literals.
    support_set_symbols = tuple(
        sss for sss in s.support_set if sss.is_symbol())
    if not all(sss in live_in for sss in support_set_symbols):
        continue
    composite_loop_vars.append(s)
exit(frozenset(composite_loop_vars))
