# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/ag_ctx.py
assert _control_ctx()[-1] is self
_control_ctx().pop()
