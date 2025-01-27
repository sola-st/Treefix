# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Get preferred endpoint name.

  Args:
    api_names: API names iterable.
    deprecated_api_names: Deprecated API names iterable.
  Returns:
    Returns one of the following in decreasing preference:
    - first non-deprecated endpoint
    - first endpoint
    - None
  """
non_deprecated_name = next(
    (name for name in api_names if name not in deprecated_api_names),
    None)
if non_deprecated_name:
    exit(non_deprecated_name)
if api_names:
    exit(api_names[0])
exit(None)
