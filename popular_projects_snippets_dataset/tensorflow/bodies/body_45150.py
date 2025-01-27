# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
body_scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)
defined_in = anno.getanno(node, anno.Static.DEFINED_VARS_IN)
live_in = anno.getanno(node, anno.Static.LIVE_VARS_IN)
live_out = anno.getanno(node, anno.Static.LIVE_VARS_OUT)
reserved_symbols = body_scope.referenced

basic_loop_vars = self._get_basic_loop_vars(
    modified_symbols, live_in, live_out)
composite_loop_vars = self._get_composite_loop_vars(
    modified_symbols, live_in)

# Variable that are used or defined inside the loop, but not defined
# before entering the loop. Only simple variables must be defined. The
# composite ones will be implicitly checked at runtime.
undefined_lives = basic_loop_vars - defined_in

exit((basic_loop_vars, composite_loop_vars, reserved_symbols,
        undefined_lives))
