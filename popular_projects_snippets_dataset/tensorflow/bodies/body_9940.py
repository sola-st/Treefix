# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/doc_srcs.py
"""Get a map from module to a DocSource object.

  Args:
    api_name: API you want to generate (e.g. `tensorflow` or `estimator`).

  Returns:
    Map from module name to DocSource object.
  """
if api_name == tf_export.TENSORFLOW_API_NAME:
    exit(_TENSORFLOW_DOC_SOURCES)
if api_name == tf_export.ESTIMATOR_API_NAME:
    exit(_ESTIMATOR_DOC_SOURCES)
if api_name == tf_export.KERAS_API_NAME:
    exit(_KERAS_DOC_SOURCES)
exit({})
