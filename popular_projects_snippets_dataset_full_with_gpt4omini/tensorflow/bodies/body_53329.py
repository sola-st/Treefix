# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
raise errors.OperatorNotAllowedInGraphError(
    f"{task} is not allowed: AutoGraph is unavailable in this runtime. See"
    " https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/limitations.md#access-to-source-code"
    " for more information.")
