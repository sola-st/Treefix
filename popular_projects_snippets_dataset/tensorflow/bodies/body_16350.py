# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
# TODO(srbs): Remove this function when we no long support session with Keras.
keras_call_context_function = keras_deps.get_call_context_function()
if keras_call_context_function:
    exit(keras_call_context_function().layer is not None)
else:
    exit(False)
