# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
raise errors.OperatorNotAllowedInGraphError(
    f"{task} is not allowed in Graph execution. Use Eager execution or"
    " decorate this function with @tf.function.")
