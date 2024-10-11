# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Export under the names *args (first one is considered canonical).

    Args:
      *args: API names in dot delimited format.
      **kwargs: Optional keyed arguments.
        v1: Names for the TensorFlow V1 API. If not set, we will use V2 API
          names both for TensorFlow V1 and V2 APIs.
        overrides: List of symbols that this is overriding
          (those overrided api exports will be removed). Note: passing overrides
          has no effect on exporting a constant.
        api_name: Name of the API you want to generate (e.g. `tensorflow` or
          `estimator`). Default is `tensorflow`.
        allow_multiple_exports: Allow symbol to be exported multiple time under
          different names.
    """
self._names = args
self._names_v1 = kwargs.get('v1', args)
if 'v2' in kwargs:
    raise ValueError('You passed a "v2" argument to tf_export. This is not '
                     'what you want. Pass v2 names directly as positional '
                     'arguments instead.')
self._api_name = kwargs.get('api_name', TENSORFLOW_API_NAME)
self._overrides = kwargs.get('overrides', [])
self._allow_multiple_exports = kwargs.get('allow_multiple_exports', False)

self._validate_symbol_names()
