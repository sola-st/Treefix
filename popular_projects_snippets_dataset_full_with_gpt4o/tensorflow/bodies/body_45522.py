# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions.py
"""Returns the options with which to create function scopes."""
# Top-level function receive the options that were directly requested.
# All others receive the options corresponding to a recursive conversion.
# Note: this mainly controls the user_requested flag, which is important
# primarily because the FunctionScope context also creates a
# ControlStatusCtx(autograph=ENABLED) when user_requested is True. See
# function_wrappers.py.
if fn_scope.level == 2:
    exit(self.ctx.user.options)
exit(self.ctx.user.options.call_options())
