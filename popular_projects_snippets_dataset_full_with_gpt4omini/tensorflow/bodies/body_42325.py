# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context manager for setting device placement policy for current thread."""
ctx = context()
old_policy = ctx.device_policy
try:
    ctx.device_policy = policy
    exit()
finally:
    ctx.device_policy = old_policy
