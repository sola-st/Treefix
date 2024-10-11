# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Add a tensor filter.

    A tensor filter is a named callable of the signature:
      filter_callable(dump_datum, tensor),

    wherein dump_datum is an instance of debug_data.DebugTensorDatum carrying
    metadata about the dumped tensor, including tensor name, timestamps, etc.
    tensor is the value of the dumped tensor as an numpy.ndarray object.
    The return value of the function is a bool.
    This is the same signature as the input argument to
    debug_data.DebugDumpDir.find().

    Args:
      filter_name: (str) name of the filter. Cannot be empty.
      filter_callable: (callable) a filter function of the signature described
        as above.

    Raises:
      ValueError: If filter_name is an empty str.
      TypeError: If filter_name is not a str.
                 Or if filter_callable is not callable.
    """

if not isinstance(filter_name, str):
    raise TypeError("Input argument filter_name is expected to be str, "
                    "but is not.")

# Check that filter_name is not an empty str.
if not filter_name:
    raise ValueError("Input argument filter_name cannot be empty.")

# Check that filter_callable is callable.
if not callable(filter_callable):
    raise TypeError(
        "Input argument filter_callable is expected to be callable, "
        "but is not.")

self._tensor_filters[filter_name] = filter_callable
