# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/signature/signature_def_utils.py
"""Sets SignatureDefs to the Metadata of a TfLite flatbuffer buffer.

  Args:
    tflite_model: Binary TFLite model (bytes or bytes-like object) to which to
      add signature_def.
    signature_def_map: dict containing SignatureDefs to store in metadata.
  Returns:
    buffer: A TFLite model binary identical to model buffer with
      metadata field containing SignatureDef.

  Raises:
    ValueError:
      tflite_model buffer does not contain a valid TFLite model.
      signature_def_map is empty or does not contain a SignatureDef.
  """
model = tflite_model
if not isinstance(tflite_model, bytearray):
    model = bytearray(tflite_model)
serialized_signature_def_map = {
    k: v.SerializeToString() for k, v in signature_def_map.items()}
model_buffer = signature_def_util.SetSignatureDefMap(
    model, serialized_signature_def_map)
exit(model_buffer)
