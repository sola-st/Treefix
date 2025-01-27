# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
raise errors.OperatorNotAllowedInGraphError(
    f"{task} is not allowed: AutoGraph is disabled in this function."
    " Try decorating it directly with @tf.function.")
