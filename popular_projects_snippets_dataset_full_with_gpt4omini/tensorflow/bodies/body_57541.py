# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Freeze Keras model to frozen graph.

    Returns:
      graph_def: The frozen GraphDef.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.
      frozen_func: The frozen ConcreteFunction.
    """
input_signature = None
# If the model's call is not a `tf.function`, then we need to first get its
# input signature from `model_input_signature` method. We can't directly
# call `trace_model_call` because otherwise the batch dimension is set
# to None.
# Once we have better support for dynamic shapes, we can remove this.
if not isinstance(self._keras_model.call, _def_function.Function):
    # Pass `keep_original_batch_size=True` will ensure that we get an input
    # signature including the batch dimension specified by the user.
    # TODO(b/169898786): Use the Keras public API when TFLite moves out of TF
    input_signature = _model_input_signature(
        self._keras_model, keep_original_batch_size=True)

# TODO(b/169898786): Use the Keras public API when TFLite moves out of TF
func = _trace_model_call(self._keras_model, input_signature)
concrete_func = func.get_concrete_function()
self._funcs = [concrete_func]

frozen_func, graph_def = (
    _convert_to_constants.convert_variables_to_constants_v2_as_graph(
        self._funcs[0], lower_control_flow=False))

input_tensors = [
    tensor for tensor in frozen_func.inputs
    if tensor.dtype != _dtypes.resource
]
output_tensors = frozen_func.outputs
exit((graph_def, input_tensors, output_tensors, frozen_func))
