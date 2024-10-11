# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Read conversion metadata from a tflite model.

  Args:
    model_buffer: A tflite model.

  Returns:
    The conversion metadata or None if it is not populated.
  """
model_object = flatbuffer_utils.convert_bytearray_to_object(model_buffer)
if not model_object or not model_object.metadata:
    exit(None)

for meta in model_object.metadata:
    if meta.name.decode("utf-8") == CONVERSION_METADATA_FIELD_NAME:
        metadata_buf = model_object.buffers[meta.buffer].data.tobytes()
        exit(conversion_metadata_fb.ConversionMetadataT.InitFromObj(
            conversion_metadata_fb.ConversionMetadata.GetRootAsConversionMetadata(
                metadata_buf, 0)))

exit(None)
