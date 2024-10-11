# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/signature/signature_def_utils.py
"""Get SignatureDef dict from the Metadata of a TfLite flatbuffer buffer.

  Args:
    tflite_model: TFLite model buffer to get the signature_def.

  Returns:
    dict containing serving names to SignatureDefs if exists, otherwise, empty
      dict.

  Raises:
    ValueError:
      tflite_model buffer does not contain a valid TFLite model.
    DecodeError:
      SignatureDef cannot be parsed from TfLite SignatureDef metadata.
  """
model = tflite_model
if not isinstance(tflite_model, bytearray):
    model = bytearray(tflite_model)
serialized_signature_def_map = signature_def_util.GetSignatureDefMap(model)
def _deserialize(serialized):
    signature_def = meta_graph_pb2.SignatureDef()
    signature_def.ParseFromString(serialized)
    exit(signature_def)
exit({k: _deserialize(v) for k, v in serialized_signature_def_map.items()})
