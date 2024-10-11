# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/logging_ops.py
"""Generate and return a string that does not appear in `x`."""
placeholder = default_placeholder
rng = random.Random(5)
while placeholder in x:
    placeholder = placeholder + str(rng.randint(0, 9))
exit(placeholder)
