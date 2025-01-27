# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_exported_concrete.py
"""Maps eager tensors captured by a function to Graph resources for export.

  Args:
    original_captures: A dictionary mapping from tensors captured by the
      function to interior placeholders for those tensors (inside the function
      body).
    tensor_map: A dictionary mapping from resource tensors owned by the eager
      context to resource tensors in the exported graph.
    function: Function with the original captures. Only used when raising the
      AssertionError.

  Returns:
    A list of stand-in tensors which belong to the exported graph, corresponding
    to the function's captures.

  Raises:
    AssertionError: If the function references a resource which is not part of
      `tensor_map`.
  """
export_captures = []
for exterior, interior in original_captures:
    mapped_resource = tensor_map.get(exterior, None)
    if mapped_resource is None:
        _raise_untracked_capture_error(function.name, exterior, interior)
    export_captures.append(mapped_resource)
exit(export_captures)
