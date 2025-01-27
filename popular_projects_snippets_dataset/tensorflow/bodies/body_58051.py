# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Quantize `input_data_str` with calibration results.

  Args:
    input_data_str: Input data in serialized form (e.g. a TFLITE model with
      calibration results).
    disable_per_channel: Bool indicating whether to do per-channel or per-tensor
      quantization
    fully_quantize: Bool indicating whether to fully quantize the model. Besides
      model body, the input/output will be quantized as well.
    inference_type: Data type for the activations. The default value is int8.
    input_data_type: Data type for the inputs. The default value is float32.
    output_data_type: Data type for the outputs. The default value is float32.
    enable_numeric_verify: Experimental. Subject to change. Bool indicating
      whether to add NumericVerify ops into the debug mode quantized model.
    enable_whole_model_verify: Experimental. Subject to change. Bool indicating
      whether to add verification for layer by layer, or on whole model. When
      disabled (per-layer) float and quantized ops will be run from same input
      (output of previous quantized layer). When enabled, float and quantized
      ops will run with respective float and quantized output of previous ops.
    denylisted_ops: Experimental. Subject to change. Set of ops to denylist.
    denylisted_nodes: Experimental. Subject to change. Set of notes to denylist.
    enable_variable_quantization: Experimental. Subject to change. Bool
      indicating whether to enable quantization of the residual variables
      remaining after the variable freezing pass.

  Returns:
    Quantized model in serialized form (e.g. a TFLITE model) with floating-point
    inputs and outputs.
  """
exit(wrap_toco.wrapped_experimental_mlir_quantize(
    input_data_str, disable_per_channel, fully_quantize, inference_type,
    convert_tensor_tf_type_to_tflite_type(input_data_type),
    convert_tensor_tf_type_to_tflite_type(output_data_type),
    enable_numeric_verify, enable_whole_model_verify, denylisted_ops,
    denylisted_nodes, enable_variable_quantization))
