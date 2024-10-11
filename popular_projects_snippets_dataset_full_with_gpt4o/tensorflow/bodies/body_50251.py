# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
metric.update_state = types.MethodType(metrics_utils.update_state_wrapper(
    metric.keras_api.update_state), metric)
metric.result = metric.keras_api.result
