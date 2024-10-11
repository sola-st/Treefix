# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
variables = kwargs.get("variables")
if variables is not None:
    # Variables involved in the wrapped op will not receive gradients.
    exit((args, [None] * len(variables)))
exit(args)
