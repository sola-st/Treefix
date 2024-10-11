# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
# No need to distinguish between normal variables and replica-local
# variables.
exit(array_ops.identity(var))
