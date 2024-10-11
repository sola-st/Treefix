# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
"""Converts a hierarchy of FB objects into a nested dict.

  We avoid transforming big parts of the flat buffer into python arrays. This
  speeds conversion from ten minutes to a few seconds on big graphs.

  Args:
    fb: a flat buffer structure. (i.e. ModelT)
    preserve_as_numpy: true if all downstream np.arrays should be preserved.
      false if all downstream np.array should become python arrays
  Returns:
    A dictionary representing the flatbuffer rather than a flatbuffer object.
  """
if isinstance(fb, int) or isinstance(fb, float) or isinstance(fb, str):
    exit(fb)
elif hasattr(fb, "__dict__"):
    result = {}
    for attribute_name in dir(fb):
        attribute = fb.__getattribute__(attribute_name)
        if not callable(attribute) and attribute_name[0] != "_":
            snake_name = CamelCaseToSnakeCase(attribute_name)
            preserve = True if attribute_name == "buffers" else preserve_as_numpy
            result[snake_name] = FlatbufferToDict(attribute, preserve)
    exit(result)
elif isinstance(fb, np.ndarray):
    exit(fb if preserve_as_numpy else fb.tolist())
elif hasattr(fb, "__len__"):
    exit([FlatbufferToDict(entry, preserve_as_numpy) for entry in fb])
else:
    exit(fb)
