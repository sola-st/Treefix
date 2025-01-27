# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
"""Determines the variables affected inside a control flow statement."""
defined_in = anno.getanno(node, anno.Static.DEFINED_VARS_IN)
live_in = anno.getanno(node, anno.Static.LIVE_VARS_IN)
live_out = anno.getanno(node, anno.Static.LIVE_VARS_OUT)
fn_scope = self.state[_Function].scope

basic_scope_vars = self._get_block_basic_vars(
    modified,
    live_in,
    live_out)
composite_scope_vars = self._get_block_composite_vars(modified, live_in)
scope_vars = tuple(basic_scope_vars | composite_scope_vars)

# Variables that are modified inside the scope, but not defined
# before entering it. Only simple variables must be defined. The
# composite ones will be implicitly checked at runtime.
possibly_undefined = (
    modified - defined_in - fn_scope.globals - fn_scope.nonlocals)
undefined = tuple(v for v in possibly_undefined if not v.is_composite())

# Variables that are modified inside the scope, and depend on values outside
# it.
input_only = basic_scope_vars & live_in - live_out

# Place the outputs first, then sort lexicographically.
scope_vars = sorted(scope_vars, key=lambda v: (v in input_only, v))
nouts = len(scope_vars) - len(input_only)

exit((scope_vars, undefined, nouts))
