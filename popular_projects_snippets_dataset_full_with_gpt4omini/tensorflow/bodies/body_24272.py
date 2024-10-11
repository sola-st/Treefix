# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Add a tensor filter.

    Args:
      filter_name: (`str`) name of the filter.
      tensor_filter: (`callable`) the filter callable. See the doc string of
        `DebugDumpDir.find()` for more details about its signature.
    """

self._tensor_filters[filter_name] = tensor_filter
