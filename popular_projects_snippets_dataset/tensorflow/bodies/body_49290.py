# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
control_status = ag_ctx.control_status_ctx()
ag_result = autograph.tf_convert(obj_result, control_status)
exit(ag_result(*args, **kwargs))
