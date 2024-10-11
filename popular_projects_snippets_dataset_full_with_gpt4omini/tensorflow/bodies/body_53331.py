# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
raise errors.OperatorNotAllowedInGraphError(
    f"{task} is not allowed: AutoGraph did convert this function. This"
    " might indicate you are trying to use an unsupported feature.")
