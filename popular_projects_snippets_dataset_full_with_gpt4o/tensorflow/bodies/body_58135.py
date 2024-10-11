# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Add or update conversion metadata to a tflite model.

  Args:
    model_object: A tflite model in object form.
    metadata: The conversion metadata.

  Returns:
    A tflite model object with embedded conversion metadata.
  """
try:
    metadata_builder = flatbuffers.Builder(0)
    metadata_builder.Finish(metadata.Pack(metadata_builder))
    buffer_field = schema_fb.BufferT()
    buffer_field.data = metadata_builder.Output()

    if not model_object.metadata:
        model_object.metadata = []
    else:
        # Check if metadata has already been populated.
        for meta in model_object.metadata:
            if meta.name.decode("utf-8") == CONVERSION_METADATA_FIELD_NAME:
                model_object.buffers[meta.buffer] = buffer_field
                exit(model_object)

    if not model_object.buffers:
        model_object.buffers = []
    model_object.buffers.append(buffer_field)
    # Creates a new metadata field.
    metadata_field = schema_fb.MetadataT()
    metadata_field.name = CONVERSION_METADATA_FIELD_NAME
    metadata_field.buffer = len(model_object.buffers) - 1
    model_object.metadata.append(metadata_field)

    exit(model_object)
except Exception:  # pylint: disable=broad-except
    exit(model_object)
