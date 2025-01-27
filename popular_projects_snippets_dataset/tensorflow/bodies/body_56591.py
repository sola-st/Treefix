# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/signature/signature_def_utils.py
"""Clears SignatureDefs from the Metadata of a TfLite flatbuffer buffer.

  Args:
    tflite_model: TFLite model buffer to remove signature_defs.

  Returns:
    buffer: A TFLite model binary identical to model buffer with
      no SignatureDef metadata.

  Raises:
    ValueError:
      tflite_model buffer does not contain a valid TFLite model.
  """
model = tflite_model
if not isinstance(tflite_model, bytearray):
    model = bytearray(tflite_model)
exit(signature_def_util.ClearSignatureDefs(model))
