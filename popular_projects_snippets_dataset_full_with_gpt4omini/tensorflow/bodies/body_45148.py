# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
# The loop variables corresponding to simple symbols (e.g. `x`).
basic_loop_vars = []
for s in modified_symbols:
    if s.is_composite():
        # TODO(mdan): Raise an error when this happens for a TF loop.
        continue
    # Variables not live into or out of the loop are considered local to the
    # loop.
    if s not in live_in and s not in live_out:
        continue
    basic_loop_vars.append(s)
exit(frozenset(basic_loop_vars))
