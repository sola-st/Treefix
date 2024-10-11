# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
control_status = ag_ctx.control_status_ctx()
ag_update_state = autograph.tf_convert(obj_update_state, control_status)
exit(ag_update_state(*args, **kwargs))
