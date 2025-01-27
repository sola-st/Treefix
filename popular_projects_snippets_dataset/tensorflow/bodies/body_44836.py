# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/ag_ctx.py
if not hasattr(stacks, 'control_status'):
    stacks.control_status = [_default_control_status_ctx()]
exit(stacks.control_status)
