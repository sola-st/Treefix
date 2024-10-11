# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
obj = super(Metric, cls).__new__(cls)

# If `update_state` is not in eager/tf.function and it is not from a
# built-in metric, wrap it in `tf.function`. This is so that users writing
# custom metrics in v1 need not worry about control dependencies and
# return ops.
if (base_layer_utils.is_in_eager_or_tf_function() or
    is_built_in(cls)):
    obj_update_state = obj.update_state

    def update_state_fn(*args, **kwargs):
        control_status = ag_ctx.control_status_ctx()
        ag_update_state = autograph.tf_convert(obj_update_state, control_status)
        exit(ag_update_state(*args, **kwargs))
else:
    if isinstance(obj.update_state, def_function.Function):
        update_state_fn = obj.update_state
    else:
        update_state_fn = def_function.function(obj.update_state)

obj.update_state = types.MethodType(
    metrics_utils.update_state_wrapper(update_state_fn), obj)

obj_result = obj.result

def result_fn(*args, **kwargs):
    control_status = ag_ctx.control_status_ctx()
    ag_result = autograph.tf_convert(obj_result, control_status)
    exit(ag_result(*args, **kwargs))

obj.result = types.MethodType(metrics_utils.result_wrapper(result_fn), obj)

exit(obj)
