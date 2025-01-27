# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
try:
    exit(var_name == item.op.name)
except AttributeError:
    # Collection items without operation are ignored.
    exit(False)
